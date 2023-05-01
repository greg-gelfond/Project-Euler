"""
Sum Square Difference
Project Euler - Problem 6

Problem Description:

The sum of the squares of the first ten natural numbers is:

        1^2 + 2^2 + 3^2 + 4^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is:

        (1 + 2 + 3 + 4 + ... + 10)^2 = 3025

Hence the difference between the sum of the squares of the first ten natural
numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
natural numbers and the square of the sum.
"""

# Let S1 be the sum of the squares of the first ten natural numbers.
S1 = sum([x**2 for x in range(1, 101)])

# Let S2 be the square of the sum of the first ten natural numbers.
S2 = sum(list(range(1, 101))) ** 2

# compute and print the difference between S1 and S2
print(abs(S1 - S2))
