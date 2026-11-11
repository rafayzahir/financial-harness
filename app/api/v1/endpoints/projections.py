
from fastapi import APIRouter, HTTPException

from app.schemas.projections import (
    InvestmentProjectionRequest,
    InvestmentProjectionResponse,
)
from app.services.portfolio.projections import (
    calculate_investment_projection,
)

router = APIRouter(tags=["Investment Projections"])


@router.post(
    "/",
    response_model=InvestmentProjectionResponse,
)
def create_investment_projection(
    request: InvestmentProjectionRequest,
):
    try:
        return calculate_investment_projection(
            initial_investment=request.initial_investment,
            monthly_contribution=request.monthly_contribution,
            annual_return_rate=request.annual_return_rate,
            years=request.years,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc
