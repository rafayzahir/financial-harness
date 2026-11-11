
from datetime import datetime, timezone

from fastapi import APIRouter, HTTPException, Query

from app.services.fundamentals.comparison import compare_companies

router = APIRouter(tags=["Stock Comparison"])


@router.get("/")
def compare_stocks(
    symbols: list[str] = Query(
        ...,
        min_length=2,
        max_length=5,
        description="Company symbols, e.g. AAPL, MSFT",
    ),
):
    try:
        results = compare_companies(symbols)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return {
        "comparison": results,
        "source": "Finnhub",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
