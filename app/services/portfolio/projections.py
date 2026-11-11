
def calculate_investment_projection(
    initial_investment: float,
    monthly_contribution: float,
    annual_return_rate: float,
    years: int,
):
    if initial_investment < 0:
        raise ValueError("Initial investment cannot be negative")

    if monthly_contribution < 0:
        raise ValueError("Monthly contribution cannot be negative")

    if annual_return_rate <= -100:
        raise ValueError("Annual return rate must be greater than -100%")

    if not 1 <= years <= 100:
        raise ValueError("Years must be between 1 and 100")

    months = years * 12
    monthly_rate = (1 + annual_return_rate / 100) ** (1 / 12) - 1

    if monthly_rate == 0:
        future_initial = initial_investment
        future_contributions = monthly_contribution * months
    else:
        future_initial = (
            initial_investment * (1 + monthly_rate) ** months
        )

        future_contributions = (
            monthly_contribution
            * (((1 + monthly_rate) ** months - 1) / monthly_rate)
        )

    future_value = future_initial + future_contributions
    total_invested = initial_investment + monthly_contribution * months

    return {
        "initial_investment": round(initial_investment, 2),
        "monthly_contribution": round(monthly_contribution, 2),
        "annual_return_rate": annual_return_rate,
        "years": years,
        "total_invested": round(total_invested, 2),
        "projected_value": round(future_value, 2),
        "estimated_gain": round(future_value - total_invested, 2),
    }
