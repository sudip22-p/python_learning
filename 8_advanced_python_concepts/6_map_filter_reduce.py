#  MAP
# Applies a function to each item in an iterable (like a list)


def square(x):
    return x * x


numbers = [1, 2, 3, 4]
squared = list(map(square, numbers))  # Applies square() to each item
print("Squared:", squared)  # Output: [1, 4, 9, 16]


#  FILTER
# Filters items in an iterable based on a condition


def is_even(x):
    return x % 2 == 0


evens = list(filter(is_even, numbers))  # Keeps only even numbers
print("Evens:", evens)  # Output: [2, 4]


#  REDUCE
# Applies a function cumulatively to the items of a sequence
# Must import from functools

from functools import reduce


def add(x, y):
    return x + y


total = reduce(add, numbers)  # (((1+2)+3)+4)
print("Sum:", total)  # Output: 10
