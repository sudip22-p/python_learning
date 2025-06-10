# Sets are unordered collections of unique elements
fruits = {"apple", "banana", "mango", "apple"}  # duplicates are ignored
print("Fruits set:", fruits)  # Only one 'apple' will appear

# Adding and removing elements
fruits.add("orange")  # Add new item
fruits.discard("banana")  # Remove item if exists (no error if it doesn't)
print("Updated fruits:", fruits)

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

print("Union:", set1 | set2)  # All unique elements
print("Intersection:", set1 & set2)  # Common elements
print("Difference:", set1 - set2)  # Elements in set1 not in set2
print("Symmetric Difference:", set1 ^ set2)  # Elements not common

# Use case: Remove duplicates from a list
nums = [1, 2, 2, 3, 4, 4, 5]
unique_nums = list(set(nums))
print("Unique numbers:", unique_nums)
