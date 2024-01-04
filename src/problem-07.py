"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
the 6th prime is 13.

What is the 10001st prime number?
"""

from math import floor, sqrt


def is_prime(x: int) -> bool:
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


def nth_prime(n: int) -> int:
    """
    Returns the nth prime.
    """
    i, j, x = 0, 0, 0
    while j < n:
        if is_prime(i):
            x, j = i, j + 1
        i += 1
    return x


def solution() -> int:
    """
    Returns the 10001st prime number.
    """
    return nth_prime(10001)


if __name__ == "__main__":
    print(solution())
