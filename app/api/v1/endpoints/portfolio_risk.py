
from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.api.deps import get_current_user
from app.db.session import get_db
from app.models.portfolio import PortfolioHolding
from app.models.user import User
from app.services.portfolio.risk import analyze_portfolio_risk

router = APIRouter(tags=["Portfolio Risk"])


@router.get("/risk")
def get_portfolio_risk(
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
        risk_analysis = analyze_portfolio_risk(holdings)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail="Unable to calculate portfolio risk",
        ) from exc

    return {
        **risk_analysis,
        "source": "Finnhub",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
