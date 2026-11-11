
from app.sandbox.executor import SafePythonExecutor
from app.sandbox.validator import SandboxValidationError

sandbox = SafePythonExecutor()


def test_normal_calculations():
    print("\n1. Normal calculations")

    assert sandbox.execute("100000 * 0.12") == 12000.0
    assert sandbox.execute("sum([10, 20, 30])") == 60
    assert sandbox.execute("(150 - 100) / 100 * 100") == 50.0

    print("PASSED: All normal calculations")


def test_malicious_expression():
    print("\n2. Malicious expression")

    try:
        sandbox.execute("__import__(chr(111)+chr(115))")
        raise AssertionError("Unsafe expression was executed.")
    except SandboxValidationError:
        print("PASSED: Restricted function blocked")


def test_power_limit():
    print("\n3. Power operation limit")

    try:
        sandbox.execute("2 ** 101")
        raise AssertionError("Power limit was not enforced.")
    except SandboxValidationError as error:
        print(f"PASSED: {error}")


def test_repetition_limit():
    print("\n4. String repetition limit")

    try:
        sandbox.execute("'a' * 10001")
        raise AssertionError("Repetition limit was not enforced.")
    except SandboxValidationError as error:
        print(f"PASSED: {error}")


if __name__ == "__main__":
    test_normal_calculations()
    test_malicious_expression()
    test_power_limit()
    test_repetition_limit()

    print("\nAll sandbox tests completed successfully!")
