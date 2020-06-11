"""Misc functions related to prime numbers."""

import math

def is_prime(n):
    """Return True if n is prime else False.

    Simple primality test algorithm meant for small values of n."""
    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n) + 1), 6): # step is 6 for the 6k +- 1 method
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True

def test_is_prime():
    """Basic tests for is_prime() function."""
    
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    for n in primes:
        actual = is_prime(n)
        expected = True
        assert actual == expected,\
               f"n = {n}: actual {actual}, expected {expected}"

    non_primes = set([i for i in range(1, 21)]) - set(primes)
    for n in non_primes:
        actual = is_prime(n)
        expected = False
        assert actual == expected,\
               f"n = {n}: actual {actual}, expected {expected}"

    larger_n = 500
    larger_primes = eratosthenes(larger_n)
    for n in larger_primes:
        actual = is_prime(n)
        expected = True
        assert actual == expected,\
               f"n = {n}: actual {actual}, expected {expected}"

    larger_non_primes = set([i for i in range(1, larger_n + 1)]) - \
                        set(larger_primes)
    for n in larger_non_primes:
        actual = is_prime(n)
        expected = False
        assert actual == expected,\
               f"n = {n}: actual {actual}, expected {expected}"
    
    

def eratosthenes(n):
    """Return a list of all prime numbers less than or equal to n, using the
    sieve of Eratosthenes algorithm."""
    primes = [True for i in range(n)]
    primes[0] = False
    primes[1] = False
    
    for i in range(2, n):
        if primes[i] == True:
            j = i + i
            while j < n:
                primes[j] = False
                j += i
    returned_primes = []
    for i in range(len(primes)):
        if primes[i] == True:
            returned_primes.append(i)
    return returned_primes

def solman(n):
    prime = [False, False] + [True] * (n - 1)
    for index in range(2, n // 2):
        if prime[index]:
            for multiple in range(2 * index, n + 1, index): # sets the step to i--so the builtin increments to the next multiple without needing a while loop
                prime[multiple] = False
    primes = []
    for index in range(2, n + 1):
        if prime[index]:
             primes.append(index)
    return primes

def main():
    
    test_is_prime()
    n = 12
    expected = [2, 3, 5, 7, 11]
    actual = eratosthenes(n)
    assert actual == expected, f"actual {actual}, expected {expected}"

    print(solman(20))

    ##print(eratosthenes(100))

if __name__ == '__main__':
    main()
