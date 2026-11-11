
import ast


ALLOWED_NODES = (
    ast.Expression,
    ast.Constant,
    ast.Name,
    ast.Load,
    ast.BinOp,
    ast.UnaryOp,
    ast.Add,
    ast.Sub,
    ast.Mult,
    ast.Div,
    ast.FloorDiv,
    ast.Mod,
    ast.Pow,
    ast.USub,
    ast.UAdd,
    ast.List,
    ast.Tuple,
    ast.Call,
)

ALLOWED_FUNCTIONS = {
    "abs",
    "round",
    "min",
    "max",
    "sum",
    "len",
}


class SandboxValidationError(ValueError):
    pass


def validate_expression(expression: str) -> ast.Expression:
    if not expression or len(expression) > 2000:
        raise SandboxValidationError("Invalid expression length.")

    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise SandboxValidationError("Invalid Python expression.") from exc

    for node in ast.walk(tree):
        if not isinstance(node, ALLOWED_NODES):
            raise SandboxValidationError(
                f"Operation not allowed: {type(node).__name__}"
            )

        if isinstance(node, ast.Name):
            if node.id not in ALLOWED_FUNCTIONS:
                raise SandboxValidationError(
                    f"Name not allowed: {node.id}"
                )

        if isinstance(node, ast.Call):
            if not isinstance(node.func, ast.Name):
                raise SandboxValidationError("Only approved functions are allowed.")

            if node.func.id not in ALLOWED_FUNCTIONS:
                raise SandboxValidationError("Function not allowed.")

            if node.keywords:
                raise SandboxValidationError(
                    "Keyword arguments are not allowed."
                )

    return tree
