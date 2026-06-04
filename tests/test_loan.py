import pytest
from app.core.loan import monthly_repayment

def test_zero_interest():
    assert monthly_repayment(1200, 0, 12) == 100.0

def test_standard_case():
    result = monthly_repayment(100000, 10, 12)
    assert result > 0

def test_loan_invalid_months():
    with pytest.raises(ValueError):
        monthly_repayment(100000, 10, 0)

def test_loan_invalid_principal():
    with pytest.raises(ValueError):
        monthly_repayment(-1000, 10, 12)