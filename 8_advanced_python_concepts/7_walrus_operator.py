# Walrus Operator
# The walrus operator (:=) allows you to assign a value to a variable as part of an expression.
sample_data = [
    {"userId": 1, "name": "rahul", "completed": False},
    {"userId": 1, "name": "rohit", "completed": False},
    {"userId": 1, "name": "ram", "completed": False},
    {"userId": 1, "name": "ravan", "completed": True},
]

print("With Python 3.8 Walrus Operator:")
for entry in sample_data:
    if name := entry.get("name"):
        print(f'Found name: "{name}"')

print("Without Walrus operator:")
for entry in sample_data:
    name = entry.get("name")
    if name:
        print(f'Found name: "{name}"')
