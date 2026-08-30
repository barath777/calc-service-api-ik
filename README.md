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
```
## Run with Docker

Build the Docker image:

```bash
docker build -t calculation-service .
```
Run the container:
```bash
docker run -p 8000:8000 calculation-service
```
## Running Tests

Automated tests are provided using pytest to validate normal, edge, and invalid input scenarios for all calculations.

To run the test suite from the project root directory:

```bash
pytest
```

Alternatively, you can run:
```bash
python -m pytest
```
Tests cover:

- Valid input scenarios
- Edge cases (0, 1, negative values where applicable)
- Invalid input handling

## API Endpoints

### Fibonacci
GET /fibonacci/{n}

- Returns the nth Fibonacci number
- n must be a non-negative integer

Example:
GET /fibonacci/10 → { "result": 55 }

---

### Factorial
GET /factorial/{n}

- Returns factorial of n (n!)
- n must be a non-negative integer
- Includes safe upper bound to prevent performance issues

Example:
GET /factorial/5 → { "result": 120 }

---

### Loan Repayment
POST /loan

- Calculates monthly repayment using standard amortization formula
- The loan parameters are provided as a JSON request body.
## Request Body
{
  "principal": 100000,
  "annual_rate": 10,
  "months": 12
}

## Parameters
- principal — Loan principal amount. Must be greater than zero.
- annual_rate — Annual interest rate expressed as a percentage.
- months — Loan duration in months. Must be greater than zero.

Example:
10 = 10% annual interest
5.5 = 5.5% annual interest

POST /loan
{
  "principal": 100000,
  "annual_rate": 10,
  "months": 12
}

Response:
{
  monthly_payment: 8791.59
}

Invalid loan values result in a 400 Bad Request response.

For example:

{
  "principal": 10000,
  "annual_rate": 10,
  "months": 0
}

returns a 400 Bad Request response because the loan duration must be greater than zero.

## Project Packaging

This project includes a `setup.py` file to make the application installable as a Python package.

It enables clean imports across modules (e.g., `app.core`) and ensures the project can be executed consistently across different environments using:

```bash
pip install -e .
```

## Continuos Integration

GitHub Actions is used to automatically run the test suite on every push to the main branch, helping maintain code quality and prevent regressions.

## Assumptions

- Fibonacci input (`n`) must be a non-negative integer.
- Factorial input (`n`) must be a non-negative integer.
- Loan principal must be greater than zero.
- Loan duration (`months`) must be greater than zero.
- Annual interest rate (`annual_rate`) is provided as a percentage value.
  - Example: `10` represents 10% annual interest.
  - Example: `5.5` represents 5.5% annual interest.
- Financial calculations are rounded to 2 decimal places.

## Limitations

- No authentication or authorization is implemented.
- No database or persistence layer is included.
- Factorial calculations are restricted to a safe upper limit to prevent excessive resource consumption.
- This service is intended as a demonstration project and is not intended for production financial decision-making.