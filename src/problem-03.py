"""
Largest Prime Factor
Project Euler - Problem 3

Problem Description:

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
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


def prime_divisor(x, n):
    """
    Returns True if and only if x is a prime divisor of n.
    """
    return x != 0 and n % x == 0 and is_prime(x)


# print the largest prime factor of 600851475143
print(
    max(
        [
            x
            for x in range(1, int(sqrt(600851475143)) + 1)
            if prime_divisor(x, 600851475143)
        ]
    )
)
