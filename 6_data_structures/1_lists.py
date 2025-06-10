# A list is an ordered, mutable collection of items
fruits = ["apple", "banana", "mango"]

# Accessing elements (index starts at 0)
print(fruits[0])  # apple
print(fruits[-1])  # mango (negative index = from end)

# Slicing
print(fruits[1:])  # ['banana', 'mango']
print(fruits[:2])  # ['apple', 'banana']

# Looping through a list
for fruit in fruits:
    print("I like", fruit)

# Check for existence
if "banana" in fruits:
    print("🍌 Banana is in the list!")

# List can store mixed types
random_stuff = [42, "hello", 3.14, True]
print(random_stuff)

# Nested lists
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][0])  # 3 (2nd row, 1st column)

# Lists are mutable (changeable)
fruits[0] = "orange"
print(fruits)  # ['orange', 'banana', 'mango']
