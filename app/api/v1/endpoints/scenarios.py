
from fastapi import APIRouter, HTTPException

from app.schemas.scenarios import ScenarioRequest, ScenarioResponse
from app.services.portfolio.scenarios import compare_investment_scenarios

router = APIRouter(tags=["Investment Scenarios"])


@router.post("/", response_model=ScenarioResponse)
def create_scenarios(request: ScenarioRequest):
    try:
        return compare_investment_scenarios(
            initial_investment=request.initial_investment,
            monthly_contribution=request.monthly_contribution,
            years=request.years,
            annual_return_rates=request.annual_return_rates,
        )
    except ValueError as exc:
        raise HTTPException(
            status_code=400,
            detail=str(exc),
        ) from exc
