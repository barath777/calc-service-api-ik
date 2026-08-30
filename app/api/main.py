from fastapi import FastAPI
from app.core.fibonacci import fibonacci
from app.core.factorial import factorial
from app.core.loan import monthly_repayment
from pydantic import BaseModel, Field

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

class LoanRequest(BaseModel):
    # principal: float = Field(..., ge=0, description="Loan Principal(>=0)")
    # annual_rate: float = Field(..., ge=0, description="Annual interest rate in percent (>= 0)")
    # months: int = Field(..., gt=0, description="Number of months(> 0)")
    principal: float 
    annual_rate: float
    months: int

@app.post("/loan")
def post_loan(req: LoanRequest):
    try:
        monthly = monthly_repayment(req.principal, req.annual_rate, req.months)
        return {"monthly_payment": monthly}
    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )