
import math
from typing import Any

from app.agents.tools.base import BaseTool


class RiskAnalysisTool(BaseTool):
    name = "risk_analysis"

    description = (
        "Calculate annualized volatility, Sharpe ratio "
        "and maximum drawdown from historical periodic returns."
    )

    parameters = {
        "type": "object",
        "properties": {
            "returns": {
                "type": "array",
                "items": {"type": "number"},
                "description": "Historical decimal returns, e.g. 0.02 for 2%.",
            },
            "risk_free_rate": {
                "type": "number",
                "description": "Annual risk-free rate as a decimal.",
            },
            "periods_per_year": {
                "type": "integer",
                "description": "Number of return periods per year, e.g. 252 for daily.",
            },
        },
        "required": ["returns", "risk_free_rate", "periods_per_year"],
    }

    async def execute(self, **kwargs: Any) -> dict[str, Any]:
        returns = [float(x) for x in kwargs["returns"]]
        risk_free_rate = float(kwargs["risk_free_rate"])
        periods = int(kwargs["periods_per_year"])

        if len(returns) < 2:
            raise ValueError("At least two return observations are required.")

        if periods <= 0:
            raise ValueError("periods_per_year must be positive.")

        if not all(math.isfinite(x) and x >= -1 for x in returns):
            raise ValueError("Returns must be finite and cannot be below -100%.")

        if not math.isfinite(risk_free_rate) or risk_free_rate < 0:
            raise ValueError("Risk-free rate must be finite and non-negative.")

        mean_return = sum(returns) / len(returns)

        variance = sum(
            (x - mean_return) ** 2 for x in returns
        ) / (len(returns) - 1)

        periodic_volatility = math.sqrt(variance)
        annualized_volatility = periodic_volatility * math.sqrt(periods)

        periodic_risk_free = (
            (1 + risk_free_rate) ** (1 / periods) - 1
        )

        sharpe_ratio = (
            (mean_return - periodic_risk_free) / periodic_volatility
            * math.sqrt(periods)
            if periodic_volatility > 0 else None
        )

        equity = 1.0
        peak = 1.0
        max_drawdown = 0.0

        for value in returns:
            equity *= (1 + value)
            peak = max(peak, equity)

            if peak > 0:
                drawdown = (peak - equity) / peak
                max_drawdown = max(max_drawdown, drawdown)

        return {
            "annualized_volatility": round(annualized_volatility, 6),
            "sharpe_ratio": (
                round(sharpe_ratio, 4)
                if sharpe_ratio is not None else None
            ),
            "maximum_drawdown": round(max_drawdown, 6),
            "observations": len(returns),
            "is_simulation": True,
        }
