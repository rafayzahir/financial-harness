
from typing import Any

from app.agents.tools.base import BaseTool


class CapitalAllocationTool(BaseTool):
    name = "capital_allocation"

    description = (
        "Calculate capital allocation across assets using "
        "user-provided target weights."
    )

    parameters = {
        "type": "object",
        "properties": {
            "capital": {
                "type": "number",
                "description": "Total available investment capital.",
            },
            "allocations": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "asset": {"type": "string"},
                        "weight": {"type": "number"},
                    },
                    "required": ["asset", "weight"],
                },
            },
        },
        "required": ["capital", "allocations"],
    }

    async def execute(self, **kwargs: Any) -> dict[str, Any]:
        capital = float(kwargs["capital"])
        allocations = kwargs["allocations"]

        if capital <= 0:
            raise ValueError("Capital must be greater than zero.")

        if not allocations:
            raise ValueError("Allocations cannot be empty.")

        total_weight = sum(float(x["weight"]) for x in allocations)

        if any(float(x["weight"]) < 0 for x in allocations):
            raise ValueError("Allocation weights cannot be negative.")

        if abs(total_weight - 100) > 0.01:
            raise ValueError("Allocation weights must total 100%.")

        results = []

        for item in allocations:
            weight = float(item["weight"])

            results.append({
                "asset": item["asset"],
                "weight_percentage": weight,
                "allocated_capital": round(
                    capital * weight / 100, 2
                ),
            })

        return {
            "total_capital": capital,
            "allocations": results,
            "total_allocated": round(
                sum(x["allocated_capital"] for x in results), 2
            ),
            "is_simulation": True,
        }
