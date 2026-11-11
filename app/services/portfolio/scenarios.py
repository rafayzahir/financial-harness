
from app.services.portfolio.projections import (
    calculate_investment_projection,
)


def compare_investment_scenarios(
    initial_investment: float,
    monthly_contribution: float,
    years: int,
    annual_return_rates: list[float],
):
    if not 1 <= len(annual_return_rates) <= 5:
        raise ValueError("Provide between 1 and 5 return scenarios")

    if len(set(annual_return_rates)) != len(annual_return_rates):
        raise ValueError("Return scenarios must be unique")

    scenarios = []

    for rate in annual_return_rates:
        projection = calculate_investment_projection(
            initial_investment=initial_investment,
            monthly_contribution=monthly_contribution,
            annual_return_rate=rate,
            years=years,
        )

        scenarios.append(projection)

    scenarios.sort(key=lambda item: item["projected_value"], reverse=True)

    return {
        "scenarios": scenarios,
        "best_case": scenarios[0],
        "worst_case": scenarios[-1],
    }
