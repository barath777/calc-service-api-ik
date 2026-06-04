from fastapi import FastAPI
from app.core.fibonacci import fibonacci
from app.core.factorial import factorial
from app.core.loan import monthly_repayment
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Calculation Service")

@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/fibonacci/{n}")
def get_fibonacci(n: int):
    try:
        return {"result": fibonacci(n)}
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@app.get("/factorial/{n}")
def get_factorial(n: int):
    try:
        return {"result": factorial(n)}
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

@app.get("/loan")
def get_loan(principal: float, annual_rate: float, months: int):
    try:
        return {
            "monthly_payment": monthly_repayment(principal, annual_rate, months)
        }
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )