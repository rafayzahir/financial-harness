
from abc import ABC, abstractmethod
from typing import Any


class LLMProvider(ABC):
    """Base interface for all LLM providers."""

    @abstractmethod
    async def generate(
        self,
        messages: list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        temperature: float = 0.2,
    ) -> dict[str, Any]:
        """
        Generate an LLM response.

        Args:
            messages: Conversation messages.
            tools: Optional tool definitions.
            temperature: Response randomness.

        Returns:
            Normalized LLM response.
        """
        raise NotImplementedError
