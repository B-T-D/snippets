
# Typical iterating function:
def factors_returned(n):
    """Return the factors of positive (int) n."""
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

# Generator using yield statement:
def factors_generator(n):
    """Yield the factors of positive (int) n."""
    for i in range(1, n + 1):
        if n % i == 0:
            yield i

# Using multiple yield statements to improve efficiency:
def factors_generator_2(n):
    """Yields factors of n but not in sorted order. Only tests values up to
    the square root of n, and for each factor f found, also yields n // f
    where n // f != f."""
    f = 1
    while f * f < n: # while f < sqrt(n)
        if n % f == 0:
            yield f
            yield n // f # E.g. 5 is a factor of 100, so 100 // 5 = 20 is too.
        f += 1
    if f * f == n: # special case if n is perfect square
        yield f

# Yielding an infinite series:
def fibonacci():
    """Takes no args--yields further Fibonacci numbers infinitely.

    Will never exceed max recursion depth (the full series isn't in
    memory at the same time)."""
    a = 0
    b = 1
    while True:
        yield a
        next_fib = a + b
        a = b
        b = next_fib

def infinite_count():
    n = 0
    while True:
        n += 1
        yield n

# To access the factors of n using factors_returned() function:
n = 100
factors = factors_returned(100)
print(f"Factors of {n} returned by the traditional return-statement \
function: \n{factors}")

# To access the factors using factors_generator():
print(f"Factors of {n} yielded by factors_generator(n):")
for factor in factors_generator(n):
    print(factor)

# Calling the improved shortcut-using generator:
print(f"Factors of {n} yielded by factors_generator_2() will out of order \
but faster:")
for factor in factors_generator_2(n):
    print(factor)

# Printing infinite series of fibonacci numbers:
##for number in fibonacci():
##    print(number)

for n in infinite_count():
    print(n)




