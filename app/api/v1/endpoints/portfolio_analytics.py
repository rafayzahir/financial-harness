
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.portfolio import PortfolioHolding
from app.models.user import User
from app.services.portfolio.analytics import calculate_portfolio_analytics

router = APIRouter(tags=["Portfolio Analytics"])


@router.get("/analytics")
def get_portfolio_analytics(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    holdings = db.scalars(
        select(PortfolioHolding).where(
            PortfolioHolding.user_id == current_user.id
        )
    ).all()

    if not holdings:
        raise HTTPException(
            status_code=404,
            detail="No portfolio holdings found",
        )

    try:
        analytics = calculate_portfolio_analytics(holdings)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail="Unable to calculate portfolio analytics",
        ) from exc

    return {
        **analytics,
        "source": "Finnhub",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
