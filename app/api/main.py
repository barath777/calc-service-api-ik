# app/api/main.py

from fastapi import FastAPI
from app.core.fibonacci import fibonacci
from app.core.factorial import factorial
from app.core.loan import monthly_repayment

app = FastAPI(title="Calculation Service")

@app.get("/fibonacci/{n}")
def get_fibonacci(n: int):
    return {"result": fibonacci(n)}

@app.get("/factorial/{n}")
def get_factorial(n: int):
    return {"result": factorial(n)}

@app.get("/loan")
def get_loan(principal: float, annual_rate: float, months: int):
    return {
        "monthly_payment": monthly_repayment(principal, annual_rate, months)
    }