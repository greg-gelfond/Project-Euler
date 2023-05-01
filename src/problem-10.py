"""
Summation of Primes
Project Euler - Problem 10

Problem Description:

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import sqrt
from math import floor


def is_prime(x):
    """
    Returns True if and only if x is prime.
    """
    if x < 2:
        return False
    elif x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        return not any(x % i == 0 for i in range(3, floor(sqrt(x)) + 1, 2))


def primes(end):
    """
    Returns a generator equivalent to the list of all primes less than end.
    """
    for i in range(0, end):
        if is_prime(i):
            yield i


# Print the sum of all the primes below two million.
print(sum(primes(2000000)))
