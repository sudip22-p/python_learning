"""
Dictionaries are unordered collections of key-value pairs.
- Keys must be unique and immutable (strings, numbers, tuples)
- Values can be any data type

Syntax:
    my_dict = {"key1": "value1", "key2": "value2"}
"""

# Creating a dictionary
person = {"name": "Alice", "age": 25, "city": "New York"}

print("Person info:", person)
print("Name:", person["name"])  # Access value using key

# Add / Update key-value
person["email"] = "alice@example.com"  # Add
person["age"] = 26  # Update
print("Updated:", person)

# Remove a key
person.pop("city")  # Removes key 'city'
print("After pop:", person)

# Dictionary methods
print("Keys:", person.keys())  # dict_keys(['name', 'age', 'email'])
print("Values:", person.values())  # dict_values([...])
print("Items:", person.items())  # dict_items([...])

# Looping through dictionary
for key, value in person.items():
    print(f"{key.capitalize()}: {value}")

# Use case: counting occurrences of words in a list
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nWord frequency:", word_count)
