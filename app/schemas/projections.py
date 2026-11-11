
from pydantic import BaseModel, Field


class InvestmentProjectionRequest(BaseModel):
    initial_investment: float = Field(ge=0)
    monthly_contribution: float = Field(ge=0)
    annual_return_rate: float = Field(gt=-100, le=1000)
    years: int = Field(ge=1, le=100)


class InvestmentProjectionResponse(BaseModel):
    initial_investment: float
    monthly_contribution: float
    annual_return_rate: float
    years: int
    total_invested: float
    projected_value: float
    estimated_gain: float
