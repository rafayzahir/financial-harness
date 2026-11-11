
import ast
import math
import operator
from typing import Any

from app.sandbox.validator import (
    validate_expression,
    SandboxValidationError,
)


BINARY_OPERATORS = {
    "Add": operator.add,
    "Sub": operator.sub,
    "Mult": operator.mul,
    "Div": operator.truediv,
    "FloorDiv": operator.floordiv,
    "Mod": operator.mod,
    "Pow": operator.pow,
}

UNARY_OPERATORS = {
    "USub": operator.neg,
    "UAdd": operator.pos,
}

SAFE_FUNCTIONS = {
    "abs": abs,
    "round": round,
    "min": min,
    "max": max,
    "sum": sum,
    "len": len,
}

MAX_RESULT_SIZE = 10000
MAX_COLLECTION_ITEMS = 1000
MAX_NUMBER = 1e100


class SafePythonExecutor:
    """Safely evaluates a restricted set of Python expressions."""

    def execute(self, expression: str) -> Any:
        tree = validate_expression(expression)

        try:
            result = self._evaluate(tree.body)
            self._validate_result(result)
            return result

        except SandboxValidationError:
            raise

        except Exception as exc:
            raise ValueError(
                f"Calculation failed: {type(exc).__name__}"
            ) from exc

    def _validate_result(self, result: Any) -> None:
        """Validate final calculation results."""

        if isinstance(result, bool):
            raise SandboxValidationError(
                "Boolean results are not allowed."
            )

        if isinstance(result, (int, float)):
            if abs(result) > MAX_NUMBER:
                raise SandboxValidationError(
                    "Result exceeds allowed range."
                )

            if isinstance(result, float) and not math.isfinite(result):
                raise SandboxValidationError(
                    "Non-finite result is not allowed."
                )

        if isinstance(result, (str, list, tuple)):
            if len(result) > MAX_RESULT_SIZE:
                raise SandboxValidationError(
                    "Result size exceeds allowed limit."
                )

    def _evaluate(self, node: ast.AST) -> Any:

        if isinstance(node, ast.Constant):
            if isinstance(node.value, bool) or not isinstance(
                node.value, (int, float, str)
            ):
                raise SandboxValidationError(
                    "Constant type not allowed."
                )

            if isinstance(node.value, (int, float)):
                if abs(node.value) > MAX_NUMBER:
                    raise SandboxValidationError(
                        "Number exceeds allowed range."
                    )

                if isinstance(node.value, float) and not math.isfinite(
                    node.value
                ):
                    raise SandboxValidationError(
                        "Non-finite number is not allowed."
                    )

            if isinstance(node.value, str):
                if len(node.value) > MAX_RESULT_SIZE:
                    raise SandboxValidationError(
                        "String size exceeds allowed limit."
                    )

            return node.value

        if isinstance(node, ast.List):
            if len(node.elts) > MAX_COLLECTION_ITEMS:
                raise SandboxValidationError(
                    "Collection contains too many items."
                )

            return [
                self._evaluate(item)
                for item in node.elts
            ]

        if isinstance(node, ast.Tuple):
            if len(node.elts) > MAX_COLLECTION_ITEMS:
                raise SandboxValidationError(
                    "Collection contains too many items."
                )

            return tuple(
                self._evaluate(item)
                for item in node.elts
            )

        if isinstance(node, ast.UnaryOp):
            operation = UNARY_OPERATORS.get(
                type(node.op).__name__
            )

            if operation is None:
                raise SandboxValidationError(
                    "Unary operation not allowed."
                )

            operand = self._evaluate(node.operand)
            result = operation(operand)

            self._validate_result(result)
            return result

        if isinstance(node, ast.BinOp):
            operation = BINARY_OPERATORS.get(
                type(node.op).__name__
            )

            if operation is None:
                raise SandboxValidationError(
                    "Binary operation not allowed."
                )

            left = self._evaluate(node.left)
            right = self._evaluate(node.right)

            # Power operation protection
            if isinstance(node.op, ast.Pow):
                if not isinstance(left, (int, float)):
                    raise SandboxValidationError(
                        "Power operation requires numeric values."
                    )

                if not isinstance(right, (int, float)):
                    raise SandboxValidationError(
                        "Power operation requires numeric values."
                    )

                if abs(right) > 100 or abs(left) > 1e100:
                    raise SandboxValidationError(
                        "Power operation too large."
                    )

            # String/list/tuple repetition protection
            if (
                isinstance(node.op, ast.Mult)
                and isinstance(left, (str, list, tuple))
            ):
                if not isinstance(right, int) or isinstance(right, bool):
                    raise SandboxValidationError(
                        "Repetition count must be an integer."
                    )

                if abs(right) > MAX_RESULT_SIZE:
                    raise SandboxValidationError(
                        "Repetition limit exceeded."
                    )

                if len(left) * abs(right) > MAX_RESULT_SIZE:
                    raise SandboxValidationError(
                        "Repeated result exceeds allowed size."
                    )

            result = operation(left, right)

            self._validate_result(result)
            return result

        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise SandboxValidationError(
                    "Only approved functions are allowed."
                )

            function_name = node.func.id

            if function_name not in SAFE_FUNCTIONS:
                raise SandboxValidationError(
                    "Function not allowed."
                )

            if node.keywords:
                raise SandboxValidationError(
                    "Keyword arguments are not allowed."
                )

            arguments = [
                self._evaluate(arg)
                for arg in node.args
            ]

            result = SAFE_FUNCTIONS[function_name](*arguments)

            self._validate_result(result)
            return result

        raise SandboxValidationError(
            f"Unsupported expression: {type(node).__name__}"
        )
