"""
Simple examples of type annotation syntax.

https://www.python.org/dev/peps/pep-0484/
https://docs.python.org/3/library/typing.html
"""

def square(x: int) -> int:
    return x * x

def list_range_n(n: int) -> list:
    return [i for i in range(n)]

x = 2
expected = 4
actual = square(x)
assert actual == expected, f"actual {actual}, expected {expected}"

n = 5
expected = [0, 1, 2, 3, 4]
actual = list_range_n(n)
assert actual == expected, f"actual {actual}, expected {expected}"
