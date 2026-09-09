# cli-calculator-day1

A small, modular Python project that implements a command-line calculator with proper validation, custom exceptions, and reusable utility functions.

## Project Structure

```
cli-calculator-day1/
├── calculator.py      # CLI entry point 
├── utils.py           # Reusable functions, validators & custom exceptions
├── requirements.txt   # Dependancies (For now, no need of any dependancies)
└── README.md          # Project Info
```

## Features

- **6 arithmetic operations** — `+`, `-`, `*`, `/`, `**` (power), `%` (modulo)
- **Two modes of use** — CLI operation or one-shot CLI
- **Custom exceptions** — `InvalidInputError`, `DivisionByZeroError`, `InvalidOperationError`
- **Input validation** — numeric parsing and operator checks with clear error messages
- **Calculation history** — view, and clear past results inside the CLI operation
- **Modular design** — all logic lives in `utils.py`; `calculator.py` handles I/O only


## Helper

User can type:
| Command       | Description              |
|---------------|--------------------------|
| `help`        | Show supported operations |
| `hist`        | Show calculation history  |
| `clear`       | Clear history             |
| `exit` / `q`  | Quit the calculator       |