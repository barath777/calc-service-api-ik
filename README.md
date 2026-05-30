# Calculation Service

A small production-minded service providing:
- Fibonacci number calculation
- Factorial calculation
- Loan repayment calculation

## Tech Stack
- Python 3.11
- FastAPI
- Pytest
- Docker

## Run Locally

```bash
pip install -r requirements.txt
uvicorn app.api.main:app --reload

## Tests

Automated tests are provided using pytest to validate normal, edge, and invalid input scenarios for all calculations.

To run the test suite from the project root directory:

pytest

Alternatively, you can run:

python -m pytest

All tests should pass successfully before running the application or submitting the project.