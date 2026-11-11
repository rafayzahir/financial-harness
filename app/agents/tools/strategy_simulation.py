
import math
from typing import Any, Literal

from app.agents.tools.base import BaseTool


class StrategySimulationTool(BaseTool):
    name = "strategy_simulation"

    description = (
        "Simulate hypothetical long or short investment strategies "
        "using historical asset returns and a fixed investment capital."
    )

    parameters = {
        "type": "object",
        "properties": {
            "capital": {
                "type": "number",
                "description": "Initial investment capital.",
            },
            "returns": {
                "type": "array",
                "items": {"type": "number"},
                "description": "Historical decimal returns, e.g. 0.05 means 5%.",
            },
            "side": {
                "type": "string",
                "enum": ["long", "short"],
            },
            "transaction_cost_bps": {
                "type": "number",
                "description": "Transaction cost in basis points per period.",
            },
        },
        "required": ["capital", "returns", "side"],
    }

    async def execute(self, **kwargs: Any) -> dict[str, Any]:
        capital = float(kwargs["capital"])
        returns = [float(x) for x in kwargs["returns"]]
        side: Literal["long", "short"] = kwargs["side"]
        cost_bps = float(kwargs.get("transaction_cost_bps", 0))

        if not math.isfinite(capital) or capital <= 0:
            raise ValueError("Capital must be a positive finite number.")

        if not returns:
            raise ValueError("Historical returns cannot be empty.")

        if side not in ("long", "short"):
            raise ValueError("Side must be long or short.")

        if not math.isfinite(cost_bps) or cost_bps < 0:
            raise ValueError("Transaction cost must be non-negative.")

        if not all(math.isfinite(x) and x >= -1 for x in returns):
            raise ValueError("Invalid historical return values.")

        direction = 1 if side == "long" else -1
        transaction_cost = capital * (cost_bps / 10000)

        gross_pnl = sum(
            direction * capital * period_return
            for period_return in returns
        )

        total_cost = transaction_cost * len(returns)
        net_pnl = gross_pnl - total_cost
        ending_value = capital + net_pnl

        return {
            "strategy": side,
            "initial_capital": round(capital, 2),
            "gross_profit_loss": round(gross_pnl, 2),
            "transaction_costs": round(total_cost, 2),
            "net_profit_loss": round(net_pnl, 2),
            "ending_value": round(ending_value, 2),
            "return_percentage": round(
                (net_pnl / capital) * 100, 2
            ),
            "periods": len(returns),
            "is_simulation": True,
            "assumptions": [
                "Fixed notional exposure per period.",
                "Transaction cost charged once per period.",
                "No leverage, borrowing fees, dividends or slippage.",
                "Short-selling losses can exceed initial capital.",
            ],
        }
