# Comprehension in Python
# Comprehensions are a concise way to create lists, sets, or dictionaries from existing iterables.

# List Comprehensions
# Generating a list of even numbers from 1 to 20
evens_list = [
    i for i in range(1, 21) if i % 2 == 0
]  # List of even numbers from 1 to 20
print("List Comprehension - Evens:", evens_list)


# Set Comprehensions
unique_squares = {i * i for i in range(1, 11)}  # Set of unique squares from 1 to 10
print("Set Comprehension - Unique Squares:", unique_squares)


# Dictionary Comprehensions
res = {num: num**3 for num in range(1, 6)}
print(res)


# Nested Comprehensions
nested_squares = [
    [i * j for j in range(1, 4)] for i in range(1, 4)
]  # 3x3 multiplication table
print("Nested Comprehension - Multiplication Table:")
for row in nested_squares:
    print(row)


# Generator Expressions
gen_squares = (i * i for i in range(1, 11))  # Generator for squares from 1 to 10
print("Generator Expression - Squares:")
for square in gen_squares:
    print(square, end=" ")  # Output squares one by one
print()  # New line after generator output


# Using comprehensions with functions
def square(x):
    return x * x


# Using list comprehension with a function
squared_list = [square(i) for i in range(1, 11)]  # List of squares using a function
print("List Comprehension with Function - Squares:", squared_list)


# Using set comprehension with a function
unique_squared_set = {
    square(i) for i in range(1, 11)
}  # Set of unique squares using a function
print("Set Comprehension with Function - Unique Squares:", unique_squared_set)


# Using dictionary comprehension with a function
squared_dict_func = {
    i: square(i) for i in range(1, 11)
}  # Dictionary of squares using a function
print("Dictionary Comprehension with Function - Squares:", squared_dict_func)
