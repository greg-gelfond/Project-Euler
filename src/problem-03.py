"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
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


def is_prime_divisor(x: int, n: int) -> bool:
    """
    Returns True if and only if x is a prime divisor of n.
    """
    return x != 0 and n % x == 0 and is_prime(x)


def solution() -> int:
    """
    Returns the largest prime factor of the number 600851475143.
    """
    return max(
        [
            x
            for x in range(1, int(sqrt(600851475143)) + 1)
            if is_prime_divisor(x, 600851475143)
        ]
    )


if __name__ == "__main__":
    print(solution())
