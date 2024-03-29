"""
2520 is the smallest number that can be divided by each of the numbers from 1
to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all the
numbers from 1 to 20?
"""

from functools import reduce
from math import gcd


def lcm(x: int, y: int) -> int:
    """
    Returns the least common multiple of x and y.
    """
    return x * y // gcd(x, y)


def solution() -> int:
    """
    Returns the smallest positive number that is evenly divisible by all the
    numbers from 1 to 20
    """
    return reduce(lcm, range(1, 21))


if __name__ == "__main__":
    print(solution())
