from app.core.factorial import factorial
import pytest

def test_factorial_basic():
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(7) == 5040

def test_factorial_invalid():
    with pytest.raises(ValueError):
        factorial(-5)