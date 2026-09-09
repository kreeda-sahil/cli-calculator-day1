class CalculatorError(Exception):
    pass


class InvalidInputError(CalculatorError):

    def __init__(self, value: str) -> None:
        self.value = value
        super().__init__(f"Invalid input: '{value}' is not a valid number.")


class DivisionByZeroError(CalculatorError):

    def __init__(self) -> None:
        super().__init__("Division by zero is not allowed.")


class InvalidOperationError(CalculatorError):

    def __init__(self, operation: str) -> None:
        self.operation = operation
        super().__init__(
            f"Invalid operation: '{operation}'. "
            "Supported operations: +, -, *, /, **, %"
        )


SUPPORTED_OPERATIONS = {"+", "-", "*", "/", "**", "%"}


def validate_number(value: str) -> float:

    try:
        return float(value)
    except ValueError:
        raise InvalidInputError(value)


def validate_operation(operation: str) -> str:

    operation = operation.strip()
    if operation not in SUPPORTED_OPERATIONS:
        raise InvalidOperationError(operation)
    return operation



def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError()
    return a / b


def power(a: float, b: float) -> float:
    return a ** b


def modulo(a: float, b: float) -> float:

    if b == 0:
        raise DivisionByZeroError()
    return a % b


OPERATIONS = {
    "+":  add,
    "-":  subtract,
    "*":  multiply,
    "/":  divide,
    "**": power,
    "%":  modulo,
}


def calculate(a: float, operation: str, b: float) -> float:

    operation = validate_operation(operation)
    func = OPERATIONS[operation]
    return func(a, b)


def format_result(result: float) -> str:

    if result == int(result):
        return str(int(result))
    return f"{result:.6g}"
