# tests/test_loan.py

from app.core.loan import monthly_repayment

def test_zero_interest():
    assert monthly_repayment(1200, 0, 12) == 100.0

def test_standard_case():
    result = monthly_repayment(100000, 10, 12)
    assert result > 0