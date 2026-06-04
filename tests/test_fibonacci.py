from app.core.fibonacci import fibonacci
import pytest

def test_fibonacci_basic():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(10) == 55

def test_fibonacci_invalid():
    with pytest.raises(ValueError):
        fibonacci(-1)