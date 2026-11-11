
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException

from app.services.fundamentals.analysis import analyze_fundamentals
from app.services.market_data.finnhub import (
    get_company_metrics,
    get_company_profile,
)

router = APIRouter(tags=["Fundamental Analysis"])


@router.get("/{symbol}")
def get_fundamental_analysis(symbol: str):
    symbol = symbol.upper()

    profile = get_company_profile(symbol)

    if not profile or not profile.get("name"):
        raise HTTPException(
            status_code=404,
            detail="Company not found",
        )

    metrics = get_company_metrics(symbol)

    analysis = analyze_fundamentals(profile, metrics)

    return {
        "symbol": symbol,
        "fundamentals": analysis,
        "source": "Finnhub",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
