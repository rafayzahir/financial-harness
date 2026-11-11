
from typing import Any

from app.agents.tools.base import BaseTool
from app.agents.tools.portfolio_analysis import PortfolioAnalysisTool
from app.agents.tools.capital_allocation import CapitalAllocationTool
from app.agents.tools.risk_analysis import RiskAnalysisTool
from app.agents.tools.strategy_simulation import StrategySimulationTool


class ToolRegistry:
    """Registers and manages tools available to the AI agent."""

    def __init__(self) -> None:
        self._tools: dict[str, BaseTool] = {}

    def register(self, tool: BaseTool) -> None:
        if not tool.name:
            raise ValueError("Tool name cannot be empty.")

        if tool.name in self._tools:
            raise ValueError(f"Tool already registered: {tool.name}")

        self._tools[tool.name] = tool

    def get(self, name: str) -> BaseTool:
        if name not in self._tools:
            raise ValueError(f"Unknown tool: {name}")

        return self._tools[name]

    def get_schemas(self) -> list[dict[str, Any]]:
        return [
            tool.to_llm_schema()
            for tool in self._tools.values()
        ]

    async def execute(
        self,
        name: str,
        arguments: dict[str, Any],
    ) -> Any:
        tool = self.get(name)
        return await tool.execute(**arguments)


def create_financial_registry() -> ToolRegistry:
    """Create registry with all financial tools."""

    registry = ToolRegistry()

    registry.register(PortfolioAnalysisTool())
    registry.register(CapitalAllocationTool())
    registry.register(RiskAnalysisTool())
    registry.register(StrategySimulationTool())

    return registry
