from decimal import Decimal, getcontext

getcontext().prec = 28

def monthly_repayment(principal: float, annual_rate: float, months: int) -> float:
    if principal < 0:
        raise ValueError("principal must be >= 0")
    if months <= 0:
        raise ValueError("months must be > 0")
    if annual_rate < 0:
        raise ValueError("annual_rate must be >= 0")

    P = Decimal(str(principal))
    n = Decimal(months)
    r = Decimal(annual_rate)/Decimal(100)/Decimal(12)

    if r == 0:
        result = P/n
    else:
        result = P * (r * (1 + r) ** n) / ((1 + r) ** n - 1)
    
    return float(result.quantize(Decimal("0.01")))