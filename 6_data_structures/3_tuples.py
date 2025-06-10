"""
Tuples are immutable sequences. Once created, their elements can't be changed.
They are used when data should not be modified.
"""

# Creating a tuple
person = ("Alice", 25, "Engineer")
print("Tuple:", person)

# Accessing elements (like lists)
print("Name:", person[0])
print("Age:", person[1])

# Tuple unpacking
name, age, profession = person
print(f"{name} is a {age}-year-old {profession}")

# Nested tuple
nested = ("Bob", (1, 2, 3))
print("Nested tuple:", nested)
print("Access nested item:", nested[1][2])  # nested[1] = (1, 2, 3) so nested[1][2] = 3

# Tuples are immutable
# person[0] = "Eve"  ❌ This will raise TypeError

# Useful functions with tuples
numbers = (10, 20, 30, 20, 40)

print("Length:", len(numbers))
print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))

# Single-element tuple: note the comma
single = ("only",)
print("Single-element tuple:", single)
print("Type check:", type(single))  # <class 'tuple'>
