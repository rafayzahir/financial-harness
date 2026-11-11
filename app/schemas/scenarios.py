
from pydantic import BaseModel, Field, field_validator


class ScenarioRequest(BaseModel):
    initial_investment: float = Field(ge=0)
    monthly_contribution: float = Field(ge=0)
    years: int = Field(ge=1, le=100)
    annual_return_rates: list[float] = Field(min_length=1, max_length=5)

    @field_validator("annual_return_rates")
    @classmethod
    def validate_return_rates(cls, rates):
        if any(rate <= -100 or rate > 1000 for rate in rates):
            raise ValueError(
                "Every annual return rate must be greater than -100% "
                "and at most 1000%"
            )

        if len(set(rates)) != len(rates):
            raise ValueError("Return scenarios must be unique")

        return rates


class ScenarioResponse(BaseModel):
    scenarios: list[dict]
    best_case: dict
    worst_case: dict
