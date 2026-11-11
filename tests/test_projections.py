
import pytest

from app.services.portfolio.projections import (
    calculate_investment_projection,
)


def test_projection_without_return():
    result = calculate_investment_projection(
        initial_investment=1000,
        monthly_contribution=100,
        annual_return_rate=0,
        years=1,
    )

    assert result["total_invested"] == 2200
    assert result["projected_value"] == 2200
    assert result["estimated_gain"] == 0


def test_projection_with_return():
    result = calculate_investment_projection(
        initial_investment=1000,
        monthly_contribution=100,
        annual_return_rate=10,
        years=10,
    )

    assert result["projected_value"] > result["total_invested"]
    assert result["estimated_gain"] > 0


def test_negative_initial_investment():
    with pytest.raises(ValueError):
        calculate_investment_projection(
            initial_investment=-100,
            monthly_contribution=100,
            annual_return_rate=10,
            years=10,
        )


def test_invalid_years():
    with pytest.raises(ValueError):
        calculate_investment_projection(
            initial_investment=1000,
            monthly_contribution=100,
            annual_return_rate=10,
            years=0,
        )
