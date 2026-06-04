from decimal import Decimal, getcontext

getcontext().prec = 28

def monthly_repayment(principal: float, annual_rate: float, months: int) -> float:
    if principal < 0:
        raise ValueError("principal must be >= 0")
    if months <= 0:
        raise ValueError("months must be > 0")

    P = Decimal(str(principal))
    n = Decimal(months)

    if annual_rate == 0:
        return float(P / n)

    r = Decimal(str(annual_rate)) / Decimal("12") / Decimal("100")

    numerator = r * (1 + r) ** n
    denominator = (1 + r) ** n - 1

    M = P * (numerator / denominator)

    return float(round(M, 2))