
from datetime import datetime, timezone
from typing import Literal

from fastapi import APIRouter, HTTPException, Query

from app.services.market_data import finnhub

router = APIRouter(tags=["Market Data"])


@router.get("/quote/{symbol}")
def stock_quote(symbol: str):
    data = finnhub.get_quote(symbol)

    if not data or data.get("c") == 0:
        raise HTTPException(status_code=404, detail="Stock quote not found")

    return {
        "symbol": symbol.upper(),
        "current_price": data.get("c"),
        "change": data.get("d"),
        "percent_change": data.get("dp"),
        "high": data.get("h"),
        "low": data.get("l"),
        "open": data.get("o"),
        "previous_close": data.get("pc"),
        "source": "Finnhub",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/company/{symbol}")
def company_profile(symbol: str):
    data = finnhub.get_company_profile(symbol)

    if not data or not data.get("name"):
        raise HTTPException(status_code=404, detail="Company not found")

    return {
        "symbol": symbol.upper(),
        "company": data,
        "source": "Finnhub",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/company/{symbol}/metrics")
def company_metrics(symbol: str):
    data = finnhub.get_company_metrics(symbol)

    return {
        "symbol": symbol.upper(),
        "metrics": data,
        "source": "Finnhub",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/history/{symbol}")
def historical_prices(
    symbol: str,
    resolution: Literal["1", "5", "15", "30", "60", "D", "W", "M"] = "D",
    from_timestamp: int = Query(gt=0, alias="from"),
    to_timestamp: int = Query(gt=0, alias="to"),
):
    if from_timestamp >= to_timestamp:
        raise HTTPException(
            status_code=400,
            detail="'from' must be earlier than 'to'",
        )

    data = finnhub.get_historical_prices(
        symbol,
        resolution,
        from_timestamp,
        to_timestamp,
    )

    if data.get("s") != "ok":
        raise HTTPException(
            status_code=404,
            detail="Historical price data not found",
        )

    return {
        "symbol": symbol.upper(),
        "resolution": resolution,
        "candles": data,
        "source": "Finnhub",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
