# Working with Nested Data Structures

# Nested data: A list of dictionaries, each representing a student and their grades
students = [
    {"name": "Alice", "grades": [85, 92, 78]},
    {"name": "Bob", "grades": [79, 81, 90]},
    {"name": "Charlie", "grades": [92, 88, 95]},
]

# Accessing nested elements: print Bob's second grade
print("Bob's second grade:", students[1]["grades"][1])  # Output: 81

# Calculate average grade for each student
for student in students:
    grades = student["grades"]
    average = sum(grades) / len(grades)
    print(f"{student['name']}'s average grade: {average:.2f}")

# Real-world use case:
# Imagine this is part of a school system that tracks student grades
# You can easily update, add, or analyze nested data structures like this

# Adding a new student's record
students.append({"name": "David", "grades": [88, 90, 84]})

# Updating Alice's grades by adding a new grade
students[0]["grades"].append(91)

print("\nUpdated student list with new grades:")
for student in students:
    print(student)
