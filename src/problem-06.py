"""
The sum of the squares of the first ten natural numbers is:

        1^2 + 2^2 + 3^2 + 4^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:

        (1 + 2 + 3 + 4 + ... + 10)^2 = 3025

Hence, the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""


def solution() -> int:
    """
    Returns the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.
    """
    sum1 = sum([x**2 for x in range(1, 101)])
    sum2 = sum(list(range(1, 101))) ** 2
    return abs(sum1 - sum2)


if __name__ == "__main__":
    print(solution())
