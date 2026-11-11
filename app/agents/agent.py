
import json
from typing import Any

from pydantic import ValidationError

from app.agents.providers.base import LLMProvider
from app.agents.schemas.llm import LLMResponse
from app.agents.tools.registry import ToolRegistry


class FinancialAgent:
    """Orchestrates LLM responses and financial tool execution."""

    def __init__(
        self,
        provider: LLMProvider,
        registry: ToolRegistry,
        max_iterations: int = 5,
    ) -> None:
        self.provider = provider
        self.registry = registry
        self.max_iterations = max_iterations

    async def run(self, query: str) -> dict[str, Any]:
        if not query.strip():
            raise ValueError("User query cannot be empty.")

        messages = [
            {
                "role": "system",
                "content": (
                    "You are a financial analysis assistant. "
                    "Use available tools for calculations. "
                    "Never invent market data or claim simulated "
                    "results are real. Explain assumptions and risks. "
                    "Do not execute trades or provide guaranteed returns."
                ),
            },
            {"role": "user", "content": query},
        ]

        tool_schemas = self.registry.get_schemas()

        for iteration in range(self.max_iterations):
            raw_response = await self.provider.generate(
                messages=messages,
                tools=tool_schemas,
                temperature=0.2,
            )

            try:
                response = LLMResponse.model_validate(raw_response)
            except ValidationError as exc:
                raise ValueError(
                    "LLM returned an invalid response format."
                ) from exc

            if response.finish_reason == "error":
                raise RuntimeError("LLM provider reported an error.")

            if not response.tool_calls:
                if response.finish_reason != "stop":
                    raise RuntimeError(
                        "LLM stopped without a final answer."
                    )

                return {
                    "answer": response.content or "",
                    "tool_calls": messages,
                    "iterations": iteration + 1,
                }

            if response.finish_reason != "tool_calls":
                raise ValueError(
                    "LLM response contains tool calls with an invalid finish reason."
                )

            assistant_calls = []

            for call in response.tool_calls:
                assistant_calls.append({
                    "id": call.id,
                    "type": "function",
                    "function": {
                        "name": call.name,
                        "arguments": json.dumps(call.arguments),
                    },
                })

            messages.append({
                "role": "assistant",
                "content": response.content,
                "tool_calls": assistant_calls,
            })

            for call in response.tool_calls:
                try:
                    result = await self.registry.execute(
                        call.name,
                        call.arguments,
                    )
                    tool_result = {
                        "success": True,
                        "result": result,
                    }
                except (ValueError, KeyError, TypeError) as exc:
                    tool_result = {
                        "success": False,
                        "error": str(exc),
                    }

                messages.append({
                    "role": "tool",
                    "tool_call_id": call.id,
                    "content": json.dumps(tool_result),
                })

        raise RuntimeError(
            f"Agent reached its {self.max_iterations}-iteration limit."
        )
