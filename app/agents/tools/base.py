
from abc import ABC, abstractmethod
from typing import Any


class BaseTool(ABC):
    """Base interface for financial AI agent tools."""

    name: str = ""
    description: str = ""

    parameters: dict[str, Any] = {
        "type": "object",
        "properties": {},
        "required": [],
    }

    def to_llm_schema(self) -> dict[str, Any]:
        """Convert tool definition to LLM function-calling format."""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters,
            },
        }

    @abstractmethod
    async def execute(self, **kwargs: Any) -> Any:
        """Execute the tool asynchronously."""
        raise NotImplementedError
