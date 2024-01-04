"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which
a^2 + b^2 = c^2 For example:

        32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find
the product a * b * c.
"""

from math import floor, prod, sqrt
from typing import Callable, Tuple


def third_term(x: int, y: int) -> int:
    """
    Returns the third term, z, needed to from a Pythagorean triplet from
    x and y using the equation x^2 + y^2 = z^2.
    """
    return floor(sqrt(x**2 + y**2))


def form_pythagorean_triplet(x: int, y: int, z: int) -> bool:
    """
    Returns True if and only if x, y, and z form a Pythagorean triplet.
    """
    return x**2 + y**2 == z**2


def desired_triplet(x: int, y: int, z: int) -> bool:
    """
    Returns True if and only if x, y, and z form a Pythagorean triplet and
    their sum is equal to 1000.
    """
    return x + y + z == 1000 and form_pythagorean_triplet(x, y, z)


def find_triple(
    start: int, end: int, pred: Callable[[int, int, int], bool]
) -> Tuple[int, int, int] | None:
    """
    Returns a triple of integers (x, y, z) such that x, y, and z belong to the
    interval [start,end) and satisfy the given predicate. If no such triple can
    be found, returns None.
    """
    for x in range(start, end):
        for y in range(start, end):
            z = third_term(x, y)
            if pred(x, y, z):
                return x, y, z
    return None


def solution() -> int:
    """
    Returns the product of the elements of the Pythagorean triplet whose sum is 1000.
    """
    return prod(find_triple(1, 1000, desired_triplet))


if __name__ == "__main__":
    print(solution())
