
import httpx
from fastapi import HTTPException

from app.core.config import settings

BASE_URL = "https://finnhub.io/api/v1"


def _get(endpoint: str, params: dict | None = None):
    if not settings.FINNHUB_API_KEY:
        raise HTTPException(
            status_code=500,
            detail="Finnhub API key is not configured",
        )

    request_params = {
        "token": settings.FINNHUB_API_KEY,
        **(params or {}),
    }

    try:
        response = httpx.get(
            f"{BASE_URL}/{endpoint}",
            params=request_params,
            timeout=15.0,
        )
        response.raise_for_status()
        return response.json()

    except httpx.HTTPStatusError as exc:
        if exc.response.status_code == 429:
            raise HTTPException(
                status_code=429,
                detail="Finnhub rate limit reached",
            )
        raise HTTPException(
            status_code=502,
            detail="Finnhub market data provider error",
        )

    except httpx.RequestError:
        raise HTTPException(
            status_code=503,
            detail="Unable to connect to Finnhub",
        )


def get_quote(symbol: str):
    return _get("quote", {"symbol": symbol.upper()})


def get_company_profile(symbol: str):
    return _get("stock/profile2", {"symbol": symbol.upper()})


def get_company_metrics(symbol: str):
    return _get(
        "stock/metric",
        {"symbol": symbol.upper(), "metric": "all"},
    )


def get_historical_prices(
    symbol: str,
    resolution: str,
    from_timestamp: int,
    to_timestamp: int,
):
    return _get(
        "stock/candle",
        {
            "symbol": symbol.upper(),
            "resolution": resolution,
            "from": from_timestamp,
            "to": to_timestamp,
        },
    )
