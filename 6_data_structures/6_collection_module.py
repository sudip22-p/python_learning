# collections module in Python
# This module provides useful alternatives to built-in data types (like dict, list, set, tuple)
# Inclusions:
#   🔸 defaultdict – avoids KeyError and allows default values
#   🔸 Counter – counts frequencies efficiently

from collections import defaultdict, Counter

print("🔹 Example 1: Using defaultdict (Real-world: Counting items sold)")

# Real-World Use: Suppose you are building a grocery billing system
# where you dynamically count how many items of each type are sold.

# Normal dict would throw KeyError if key not found; defaultdict handles it safely
item_sold = defaultdict(int)  # default value is 0 for any new key

# Transactions from the day
transactions = ["apple", "banana", "apple", "orange", "banana", "banana"]

# Count sold items
for item in transactions:
    item_sold[
        item
    ] += 1  # No need to check if key exists! Automatically sets 0 if key missing, then adds 1


# Convert to normal dict just for cleaner display
print("🛒 Items sold today:", dict(item_sold))  # {'apple': 2, 'banana': 3, 'orange': 1}

print("-" * 50)

print("🔹 Example 2: Using Counter (Real-world: Counting word frequency)")

# Real-World Use: Suppose you're analyzing user reviews or blog comments
# and you want to know which words are used most frequently

review = "python is great and python is fun and easy to learn python"

# Split the sentence into words and count frequency
word_count = Counter(review.split())

print("🗣️ Word frequency in review:", word_count)  # {'python': 3, 'is': 2, ...}

# Most common word
print("🔥 Most common word:", word_count.most_common(1))  # [('python', 3)]

# You can also loop over it
for word, count in word_count.items():
    print(f"'{word}' was used {count} time(s)")

print("-" * 50)

print(
    "🔹 Bonus: Using defaultdict(list) for grouping data (Real-world: Grouping students by class)"
)

# Suppose you're storing students grouped by their class section
# You don't want to manually check if the class key exists

students = defaultdict(list)  # default value is an empty list

# (name, class_section)
data = [
    ("Alice", "A"),
    ("Bob", "B"),
    ("Charlie", "A"),
    ("David", "C"),
    ("Eve", "B"),
]

for name, section in data:
    students[section].append(name)

print("🏫 Students grouped by class:", dict(students))
# Output: {'A': ['Alice', 'Charlie'], 'B': ['Bob', 'Eve'], 'C': ['David']}
