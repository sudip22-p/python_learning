fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# append(): adds item at the end
fruits.append("orange")
print("After append:", fruits)

# insert(): inserts item at a given index
fruits.insert(1, "grape")
print("After insert at index 1:", fruits)

# remove(): removes first occurrence of value
fruits.remove("banana")
print("After remove 'banana':", fruits)

# pop(): removes and returns item at index (last by default)
last_fruit = fruits.pop()
print("Popped:", last_fruit)
print("After pop:", fruits)

# index(): returns index of first occurrence
print("Index of 'cherry':", fruits.index("cherry"))

# size(): returns number of items
print("Size of list:", len(fruits))

# count(): counts number of occurrences
print("Count of 'apple':", fruits.count("apple"))

# sort(): sorts the list in-place
fruits.sort()
print("Sorted list:", fruits)

# reverse(): reverses the list in-place
fruits.reverse()
print("Reversed list:", fruits)

# copy(): returns a shallow copy
fruits_copy = fruits.copy()
print("Copied list:", fruits_copy)

# clear(): removes all items
fruits.clear()
print("Cleared list:", fruits)
