def factorial(n: int) -> int:
    if not isinstance(n, int):
        raise ValueError("n must be an integer")
    if n < 0:
        raise ValueError("n must be >= 0")
    
    if n>5000:
        raise ValueError("n is too large to compute safely")

    result = 1
    for i in range(2, n + 1):
        result *= i

    return result