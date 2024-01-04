"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_palindrome(x: int) -> bool:
    """
    Returns True if and only if x is a palindrome.
    """
    return str(x) == str(x)[::-1]


def solution() -> int:
    """
    Returns the largest palindrome made from the product of two 3-digit numbers.
    """
    return max(
        [
            x * y
            for x in range(100, 1000)
            for y in range(100, 1000)
            if is_palindrome(x * y)
        ]
    )


if __name__ == "__main__":
    print(solution())
