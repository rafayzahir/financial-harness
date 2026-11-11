
from app.services.fundamentals.analysis import analyze_fundamentals
from app.services.market_data.finnhub import (
    get_company_metrics,
    get_company_profile,
    get_quote,
)


def compare_companies(symbols: list[str]):
    results = []

    for symbol in symbols:
        symbol = symbol.strip().upper()

        profile = get_company_profile(symbol)

        if not profile or not profile.get("name"):
            continue

        metrics = get_company_metrics(symbol)
        quote = get_quote(symbol)

        results.append({
            "symbol": symbol,
            "company": profile.get("name"),
            "current_price": quote.get("c"),
            "change_percent": quote.get("dp"),
            "fundamentals": analyze_fundamentals(profile, metrics),
        })

    if len(results) < 2:
        raise ValueError("At least two valid companies are required")

    return results
