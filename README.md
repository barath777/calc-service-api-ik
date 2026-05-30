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

# API Endpoints
Fibonacci
- GET /fibonacci/{n}
Factorial
- GET /factorial/{n}
Loan Repayment
- GET /loan?principal={value}&annual_rate={value}&months={value}