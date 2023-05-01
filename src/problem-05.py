"""
Smallest Multiple
Project Euler - Problem 5

Problem Description:

2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the
numbers from 1 to 20?
"""

from functools import reduce
from fractions import gcd


def lcm(x, y):
    """
    Returns the least common multiple of x and y.
    """
    return x * y // gcd(x, y)


# compute and print the least common multiple of the numbers in the
# interval [1,21)
print(reduce(lcm, range(1, 21)))
