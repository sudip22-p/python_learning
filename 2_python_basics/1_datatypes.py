'''
Multiline comment in Python
➡️ Assigning a value to a variable
'''

# Single line comment
# No need to declare type. Python is dynamically typed.
name = "Sud"     # string
age = 22         # integer
height = 5.8     # float
is_student = True  # boolean

# Built-in data types

# 1. Numeric Types
x = 10         # int
print(x)       # Output: 10

y = 3.14       # float
print(y)       # Output: 3.14

z = 2 + 3j     # complex
print(z)       # Output: (2+3j)

# 2. Sequence Types
greeting = "Hello, World!"  # str
print(greeting)             # Output: Hello, World!

fruits = ["apple", "banana", "cherry"]  # list
print(fruits)                           # Output: ['apple', 'banana', 'cherry']

coordinates = (10.0, 20.0)  # tuple
print(coordinates)          # Output: (10.0, 20.0)

numbers = range(1, 10)      # range
print(list(numbers))        # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

# 3. Mapping Type
person = {"name": "Alice", "age": 30}  # dict
print(person)                          # Output: {'name': 'Alice', 'age': 30}

# 4. Set Types
colors = {"red", "green", "blue"}  # set
print(colors)                      # Output: order may vary

# 5. Boolean Type
is_active = True  # bool
print(is_active)  # Output: True

# 6. None Type
nothing = None  # NoneType
print(nothing)  # Output: None

# 7. Binary Types
b = bytes([65, 66, 67])  # bytes
print(b)                 # Output: b'ABC'

binary_data = b"Hello"   # bytes literal
print(binary_data)       # Output: b'Hello'

ba = bytearray([65, 66, 67])  # bytearray
ba[0] = 97
print(ba)                # Output: bytearray(b'aBC')

# 8. Immutable Types
immutable_colors = frozenset({"red", "green", "blue"})  # frozenset
print(immutable_colors)                                 # Output: order may vary

"""
🔹 Sets and Frozen sets in Python:

- Both are unordered collections of unique elements.
- They do not preserve insertion order.
- The printed order of elements may vary due to internal hashing.
- This is normal behavior and does not affect the data itself.

✅ Solution:
- If a consistent order is needed, convert the set to a list and sort it:
"""

