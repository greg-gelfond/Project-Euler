"""
Special Pythagorean Triplet
Project Euler - Problem 9

Gregory Gelfond

Problem Description:

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which, a^2 + b^2 = c^2 For example:

        32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product a * b * c.
"""

from math import sqrt
from math import floor
from functools import reduce
from operator import mul


def third_term(x, y):
    """
    Returns the third term, z, need to from a Pythagorean triplet from
    x and y using the equation x^2 + y^2 = z^2.
    """
    return floor(sqrt(x**2 + y**2))


def form_pythagorean_triplet(x, y, z):
    """
    Returns True if and only if x, y, and z form a Pythagorean triplet.
    """
    return x**2 + y**2 == z**2


def desired_triplet(x, y, z):
    """
    Returns True if and only if x, y, and z form a Pythagorean triplet and
    their sum is equal to 1000.
    """
    return x + y + z == 1000 and form_pythagorean_triplet(x, y, z)


def find_triple(start, end, pred):
    """
    Returns a triple of integers (x, y, z) such that x, y, and z belong to
    the interval [start,end) and satisfy the given predicate, pred. If
    no such triple can be found, returns None.
    """
    for x in range(start, end):
        for y in range(start, end):
            z = third_term(x, y)
            if pred(x, y, z):
                return x, y, z
    return None


# compute and print the product of the Pythagorean triplet (x,y,z)
# whose sum is equal to 1000
print(reduce(mul, find_triple(1, 1000, desired_triplet), 1))
