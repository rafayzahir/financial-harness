
from datetime import datetime, timedelta, timezone
from math import sqrt
from statistics import stdev

from app.services.market_data.finnhub import (
    get_historical_prices,
    get_quote,
)


def calculate_returns(prices: list[float]) -> list[float]:
    return [
        (prices[i] / prices[i - 1]) - 1
        for i in range(1, len(prices))
        if prices[i - 1] != 0
    ]


def calculate_volatility(returns: list[float]) -> float | None:
    if len(returns) < 2:
        return None

    return stdev(returns) * sqrt(252) * 100


def analyze_portfolio_risk(holdings):
    if not holdings:
        return {
            "holdings": [],
            "total_market_value": 0,
            "portfolio_volatility": None,
            "concentration_index": 0,
            "risk_level": "unavailable",
        }

    end_date = datetime.now(timezone.utc)
    start_date = end_date - timedelta(days=365)

    to_timestamp = int(end_date.timestamp())
    from_timestamp = int(start_date.timestamp())

    results = []
    total_market_value = 0.0

    for holding in holdings:
        quote = get_quote(holding.ticker)
        current_price = float(quote.get("c") or 0)

        market_value = float(holding.quantity) * current_price
        total_market_value += market_value

        candles = get_historical_prices(
            holding.ticker,
            "D",
            from_timestamp,
            to_timestamp,
        )

        prices = candles.get("c", []) if candles.get("s") == "ok" else []
        returns = calculate_returns(prices)

        results.append({
            "ticker": holding.ticker,
            "market_value": market_value,
            "returns": returns,
            "volatility": calculate_volatility(returns),
        })

    weighted_returns = []

    valid_results = [
        item for item in results if len(item["returns"]) >= 2
    ]

    if valid_results and total_market_value > 0:
        common_length = min(
            len(item["returns"]) for item in valid_results
        )

        for index in range(common_length):
            daily_return = sum(
                (
                    item["market_value"] / total_market_value
                ) * item["returns"][-common_length + index]
                for item in valid_results
            )
            weighted_returns.append(daily_return)

    portfolio_volatility = calculate_volatility(weighted_returns)

    concentration_index = 0.0
    if total_market_value > 0:
        concentration_index = sum(
            (item["market_value"] / total_market_value) ** 2
            for item in results
        )

    if portfolio_volatility is None:
        risk_level = "unavailable"
    elif portfolio_volatility < 15:
        risk_level = "low"
    elif portfolio_volatility < 30:
        risk_level = "moderate"
    else:
        risk_level = "high"

    for item in results:
        item["allocation_percentage"] = (
            item["market_value"] / total_market_value * 100
            if total_market_value > 0
            else 0
        )
        item.pop("returns")

    return {
        "holdings": results,
        "total_market_value": total_market_value,
        "portfolio_volatility": portfolio_volatility,
        "concentration_index": concentration_index,
        "risk_level": risk_level,
        "period": "1 year",
    }
