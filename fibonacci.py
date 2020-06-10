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

# Basically right, book is slightly more concise:

def sm_fibonacci(n):
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

    # This would have same asymptotic time complexity as mine. 


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

print(fibonacci(10))
