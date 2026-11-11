
from datetime import datetime, timezone
from typing import Literal

from fastapi import APIRouter, HTTPException, Query

from app.services.market_data import finnhub
from app.services.technical_analysis.indicators import calculate_indicators

router = APIRouter(tags=["Technical Analysis"])


@router.get("/{symbol}/indicators")
def get_technical_indicators(
    symbol: str,
    resolution: Literal["D", "W", "M"] = "D",
    from_timestamp: int = Query(gt=0, alias="from"),
    to_timestamp: int = Query(gt=0, alias="to"),
):
    if from_timestamp >= to_timestamp:
        raise HTTPException(
            status_code=400,
            detail="'from' must be earlier than 'to'",
        )

    candles = finnhub.get_historical_prices(
        symbol,
        resolution,
        from_timestamp,
        to_timestamp,
    )

    try:
        indicators = calculate_indicators(candles)
    except ValueError as exc:
        raise HTTPException(status_code=404, detail=str(exc)) from exc

    return {
        "symbol": symbol.upper(),
        "resolution": resolution,
        "indicators": indicators,
        "source": "Finnhub",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
