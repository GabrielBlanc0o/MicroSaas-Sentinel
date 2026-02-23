# MicroSaaS-Sentinel: project overview

This document explains what each file does, how the data flows through the application, and what to modify if you want to extend the project.

## High-level purpose

MicroSaaS-Sentinel calculates basic financial indicators for a small business or micro-SaaS:

- Profit (revenue minus costs)
- Profit margin (profit divided by revenue)
- Health status (classification based on margin thresholds)

The GUI collects input values and uses the engine to compute the results.

## File-by-file explanation

### `engine.py`

**Responsibility**: business logic (no UI).

Contains the `SentinelBusiness` class.

- `__init__(name, revenue, costs)`
  - Stores business name, monthly revenue, and total monthly costs.

- `calculate_profit()`
  - Returns `revenue - costs`.

- `calculate_margin()`
  - Returns the profit margin percentage:
    - If `revenue <= 0`, returns `0` to avoid division by zero.
    - Otherwise returns `(profit / revenue) * 100`.
  - Includes a small epsilon rule so values extremely close to `0` are normalized to `0.0`.

- `get_health_status()`
  - Uses the margin to classify the business:
    - `> 25`  -> `EXCELLENT`
    - `> 10`  -> `STABLE`
    - `> 0`   -> `WARNING`
    - else    -> `CRITICAL`

This file is the best place to change the financial rules.

### `GUI.py`

**Responsibility**: user interface.

Main parts:

- `interfaz` (Tkinter `Frame`)
  - Builds the window.
  - Creates the input form.
  - Reads the values, converts to numbers, and creates a `SentinelBusiness` instance.
  - Updates the dashboard with computed values.

Key method:

- `calculate_business_health()`
  1) Reads input fields
  2) Converts them to `float`
  3) Sums expenses
  4) Creates the engine object:

```python
self.business_data = SentinelBusiness(name, revenue, total_expenses)
```

  5) Calls `update_dashboard()`

Dashboard rendering uses:

- `self.business_data.get_health_status()`
- `self.business_data.calculate_margin()`
- `self.business_data.calculate_profit()`

If the GUI is working but the numbers are incorrect, the issue is usually in `engine.py`.

### `main.py`

**Responsibility**: console-based version (reference).

This is an alternative CLI input flow that asks questions in the terminal. The GUI is the primary interface now, but `main.py` is useful to compare behavior.

### `test_engine.py`

**Responsibility**: unit tests for `engine.py`.

- Tests the profit, margin, and health status calculations.
- Includes edge cases like `revenue == 0`.

If you change the thresholds or margin rules in `engine.py`, you may need to update these tests.

### `requirements.txt`

Contains Python dependencies. In this repository it is mainly used for:

- `pytest`

Tkinter is part of the standard Python installation on Windows in most setups.

## Data flow (how the app works)

1) User opens `GUI.py`
2) User enters:
   - Business name
   - Monthly revenue
   - Expenses per category
3) GUI converts inputs to numbers and totals the expenses
4) GUI creates `SentinelBusiness` with `name`, `revenue`, `total_costs`
5) GUI displays:
   - Health status
   - Margin
   - Total revenue
   - Total costs
   - Net profit

## Common issues

- If you see `ValueError` in the GUI, it usually means a text field is empty or contains non-numeric characters.
- Do not run `pytest GUI.py`. `GUI.py` is not a test file. Use `pytest` (or `pytest test_engine.py`).

## Where to extend

- Add more expense categories:
  - Add more entries in `GUI.py` where the categories list is defined.
  - The engine does not need changes if you still pass a single total cost value.

- Change thresholds:
  - Edit `get_health_status()` in `engine.py`.
  - Update `test_engine.py` to match the new thresholds.
