import sys

from utils import (
    CalculatorError,
    InvalidInputError,
    validate_number,
    validate_operation,
    calculate,
    format_result,
    SUPPORTED_OPERATIONS,
)


HELP_TEXT = """
Supported operations:  +  -  *  /  **  %

  Enter each part when prompted, or type:
    help   — show this message
    hist   — show calculation history
    clear  — clear history
    exit   — quit the calculator
"""


history: list[str] = []


def show_history() -> None:

    if not history:
        print("  (no calculations yet)")
        return
    print("\n  ── History ──")
    for i, entry in enumerate(history, 1):
        print(f"  {i}. {entry}")
    print()



def run_once(cmd_operation: list[str]) -> None:

    if len(cmd_operation) != 3:
        print("Usage: python calculator.py <number> <operator> <number>")
        print("Example: python calculator.py 10 / 3")
        sys.exit(1)

    try:
        a = validate_number(cmd_operation[0])
        op = validate_operation(cmd_operation[1])
        b = validate_number(cmd_operation[2])
        result = calculate(a, op, b)
        print(f" {format_result(a)} {op} {format_result(b)} = {format_result(result)}")
    except CalculatorError as exc:
        print(f"Error: {exc}")
        sys.exit(1)



def prompt(label: str) -> str:

    try:
        return input(f"  {label}: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye!")
        sys.exit(0)


def cli_operation() -> None:

    print("""

    Enter the numbers and the operation you want to perform.
    
    Type 'help' for instructions or 'exit' to quit.
    
    """)

    while True:
        raw_a = prompt("Enter first number")

      
        cmd = raw_a.lower()
        if cmd in ("exit", "quit", "q"):
            print("  Goodbye!")
            break
        if cmd == "help":
            print(HELP_TEXT)
            continue
        if cmd in ("hist", "history"):
            show_history()
            continue
        if cmd == "clear":
            history.clear()
            print("  History cleared.\n")
            continue

    
        try:
            a = validate_number(raw_a)
        except InvalidInputError as exc:
            print(f" {exc}\n")
            continue

        raw_op = prompt(f"Enter operation ({', '.join(sorted(SUPPORTED_OPERATIONS))})")
        try:
            op = validate_operation(raw_op)
        except CalculatorError as exc:
            print(f" {exc}\n")
            continue

        raw_b = prompt("Enter second number")
        try:
            b = validate_number(raw_b)
        except InvalidInputError as exc:
            print(f" {exc}\n")
            continue


        try:
            result = calculate(a, op, b)
        except CalculatorError as exc:
            print(f" {exc}\n")
            continue

        expr = f"{format_result(a)} {op} {format_result(b)} = {format_result(result)}"
        history.append(expr)
        print(f"\n {expr}\n")



def main() -> None:

    if len(sys.argv) > 1:
        run_once(sys.argv[1:])
    else:
        cli_operation()


if __name__ == "__main__":
    main()
