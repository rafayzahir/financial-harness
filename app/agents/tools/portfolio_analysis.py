
from typing import Any

from app.agents.tools.base import BaseTool


class PortfolioAnalysisTool(BaseTool):
    name = "portfolio_analysis"

    description = (
        "Calculate portfolio investment value, current value, "
        "profit or loss, and percentage return."
    )

    parameters = {
        "type": "object",
        "properties": {
            "holdings": {
                "type": "array",
                "description": "List of portfolio holdings.",
                "items": {
                    "type": "object",
                    "properties": {
                        "symbol": {"type": "string"},
                        "quantity": {"type": "number"},
                        "average_cost": {"type": "number"},
                        "current_price": {"type": "number"},
                    },
                    "required": [
                        "symbol",
                        "quantity",
                        "average_cost",
                        "current_price",
                    ],
                },
            }
        },
        "required": ["holdings"],
    }

    async def execute(self, **kwargs: Any) -> dict[str, Any]:
        holdings = kwargs.get("holdings", [])

        if not isinstance(holdings, list) or not holdings:
            raise ValueError("At least one holding is required.")

        total_invested = 0.0
        current_value = 0.0
        breakdown = []

        for item in holdings:
            quantity = float(item["quantity"])
            average_cost = float(item["average_cost"])
            current_price = float(item["current_price"])

            if quantity <= 0 or average_cost <= 0 or current_price < 0:
                raise ValueError("Invalid holding values.")

            invested = quantity * average_cost
            value = quantity * current_price
            pnl = value - invested

            total_invested += invested
            current_value += value

            breakdown.append({
                "symbol": item["symbol"],
                "invested": round(invested, 2),
                "current_value": round(value, 2),
                "profit_loss": round(pnl, 2),
            })

        profit_loss = current_value - total_invested
        return_percentage = (
            (profit_loss / total_invested) * 100
        )

        return {
            "total_invested": round(total_invested, 2),
            "current_value": round(current_value, 2),
            "profit_loss": round(profit_loss, 2),
            "return_percentage": round(return_percentage, 2),
            "holdings": breakdown,
            "is_simulation": True,
        }
