
def analyze_fundamentals(profile: dict, metrics_data: dict):
    metrics = metrics_data.get("metric", {})

    def get_metric(key):
        return metrics.get(key)

    return {
        "company": profile.get("name"),
        "ticker": profile.get("ticker"),
        "industry": profile.get("finnhubIndustry"),
        "market_cap": get_metric("marketCapitalization"),
        "pe_ratio": get_metric("peBasicExclExtraTTM"),
        "eps": get_metric("epsBasicExclExtraItemsTTM"),
        "revenue_per_share": get_metric("revenuePerShareTTM"),
        "profit_margin": get_metric("netProfitMarginTTM"),
        "roe": get_metric("roeTTM"),
        "roa": get_metric("roaTTM"),
        "debt_to_equity": get_metric("totalDebt/totalEquityQuarterly"),
        "dividend_yield": get_metric("currentDividendYieldTTM"),
        "52_week_high": get_metric("52WeekHigh"),
        "52_week_low": get_metric("52WeekLow"),
    }
