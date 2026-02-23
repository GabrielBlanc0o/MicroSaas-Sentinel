# MicroSaaS-Sentinel

MicroSaaS-Sentinel is a small Python project that calculates basic financial health indicators for a micro-SaaS or small business.

It includes:
- A simple calculation engine (`engine.py`).
- A Tkinter GUI (`GUI.py`) to enter revenue and expenses and display results.
- Unit tests for the engine (`test_engine.py`).

## Requirements

- Python 3
- `pytest` (only if you want to run tests)

## How to run

Run the GUI:

```bash
python GUI.py
```

Run tests:

```bash
pytest
```

## Project files

- `engine.py`: Business logic (profit, margin, health status)
- `GUI.py`: Tkinter interface
- `main.py`: Console-based input version (reference)
- `test_engine.py`: Pytest unit tests for `engine.py`
- `requirements.txt`: Test dependency list
