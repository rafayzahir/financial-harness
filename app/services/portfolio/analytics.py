
from decimal import Decimal

from app.services.market_data.finnhub import get_quote


def calculate_portfolio_analytics(holdings):
    results = []
    totals = {}

    for holding in holdings:
        quote = get_quote(holding.ticker)
        current_price = Decimal(str(quote.get("c", 0)))

        quantity = holding.quantity
        average_buy_price = holding.average_buy_price

        investment = quantity * average_buy_price
        market_value = quantity * current_price
        profit_loss = market_value - investment

        return_percentage = (
            (profit_loss / investment) * 100
            if investment > 0
            else Decimal("0")
        )

        currency = holding.currency

        results.append({
            "holding_id": holding.id,
            "ticker": holding.ticker,
            "quantity": quantity,
            "average_buy_price": average_buy_price,
            "current_price": current_price,
            "investment": investment,
            "market_value": market_value,
            "profit_loss": profit_loss,
            "return_percentage": return_percentage,
            "currency": currency,
        })

        if currency not in totals:
            totals[currency] = {
                "total_investment": Decimal("0"),
                "total_market_value": Decimal("0"),
                "total_profit_loss": Decimal("0"),
            }

        totals[currency]["total_investment"] += investment
        totals[currency]["total_market_value"] += market_value
        totals[currency]["total_profit_loss"] += profit_loss

    for values in totals.values():
        investment = values["total_investment"]
        values["return_percentage"] = (
            values["total_profit_loss"] / investment * 100
            if investment > 0
            else Decimal("0")
        )

    return {
        "holdings": results,
        "totals_by_currency": totals,
    }
