
import pytest

from app.services.portfolio.scenarios import compare_investment_scenarios


def test_compare_investment_scenarios():
    result = compare_investment_scenarios(
        initial_investment=1000,
        monthly_contribution=100,
        years=10,
        annual_return_rates=[5, 10, 15],
    )

    assert len(result["scenarios"]) == 3
    assert result["best_case"]["annual_return_rate"] == 15
    assert result["worst_case"]["annual_return_rate"] == 5


def test_scenarios_are_sorted_by_projected_value():
    result = compare_investment_scenarios(
        initial_investment=1000,
        monthly_contribution=100,
        years=10,
        annual_return_rates=[15, 5, 10],
    )

    values = [
        scenario["projected_value"]
        for scenario in result["scenarios"]
    ]

    assert values == sorted(values, reverse=True)


def test_duplicate_return_rates():
    with pytest.raises(ValueError):
        compare_investment_scenarios(
            initial_investment=1000,
            monthly_contribution=100,
            years=10,
            annual_return_rates=[5, 5],
        )


def test_too_many_scenarios():
    with pytest.raises(ValueError):
        compare_investment_scenarios(
            initial_investment=1000,
            monthly_contribution=100,
            years=10,
            annual_return_rates=[1, 2, 3, 4, 5, 6],
        )
