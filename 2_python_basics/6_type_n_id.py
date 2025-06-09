# 🔹 type() ➤ Returns the data type of an object
x = 10
print(type(x))  # <class 'int'> → 'x' is an integer

y = [1, 2, 3]
print(type(y))  # <class 'list'> → 'y' is a list

# 🔹 id() ➤ Returns the memory address (unique identity) of the object

a = 5
b = 5
print(id(a))  # Same ID as 'b' → Python automatically caches small integers from -5 to 256 to save memory and improve performance.
# So a and b both point to the same memory location.
print(id(b))

c = [1, 2]
d = [1, 2]
print(id(c))  # Different ID → even with same values, lists are different objects ->Each time you create a new list, Python creates a new object in memory, even if the contents are the same.
# Lists are mutable, so Python does not reuse the same object to avoid unintended side effects.
print(id(d))

# 📝 Notes:
# - type() is useful for debugging and checking variable types.
# - id() helps track object identity — especially important for mutable types (list, dict, etc.).
# - If two variables have the same id, they point to the same object in memory.
