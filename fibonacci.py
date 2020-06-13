def fibonacci(n):
    """Recursively returns the nth Fibonacci number.

    Runs in exponential time--asymptotically O(2^n). Because for every value
    of n, it recomputes fib(m) for every prior value m where m < n.
    """
##    print(f"n = {n} in fib() call")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def sm_fibonacci(n):
    # Erroneously returns 1 for n = 0. 
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

    # This would have same asymptotic time complexity as mine. 

def test():
    """Quick test using builtin assert."""

    # Does the function return magic-numbered first several fib numbers
    #   correctly?
    fib = [1, 1, 2, 3, 5, 8, 13]

    expecteds = [(i + 1, fib[i]) for i in range(len(fib))]

    for e in expecteds:
        expected = e[1]
        actual = fibonacci(e[0])
        assert actual == expected, f"actual {actual}, expected {expected}"

    for e in expecteds:
        expected = e[1]
        actual = sm_fibonacci(e[0])
        assert actual == expected, f"actual {actual}, expected {expected}"

    # Does the function return 0 for n = 0?
    func = fibonacci
    expected = 0
    actual = func(0)
    assert actual == expected,\
    f"{func.__name__} fail: actual {actual}, expected {expected}"

    func = sm_fibonacci
    actual = func(0)
    assert actual == expected,\
    f"{func.__name__} fail: actual {actual}, expected {expected}"

if __name__ == '__main__':
    test()
