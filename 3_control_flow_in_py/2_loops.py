# 🔁 Control flow using loops in Python

# ✅ For loop: iterate over a list of tasks
tasks = ["wake up", "study", "code", "sleep"]

for task in tasks:
    if task == "code":
        continue  # Skip 'code' for now
    print(
        f"Task: {task}"
    )  # Executes for each item except 'code' 'f' indicates formatted string i.e. variable inside curly braces just like `` in javascript
else:  # why else after for loop?
    # because it runs when the loop completes naturally
    print("✅ Finished all tasks in for loop")

print("-" * 40)  # 40 dashes for separation

# ✅ While loop: countdown simulation
countdown = 3

while countdown > 0:
    print(f"Event starts in {countdown} seconds...")
    countdown -= 1  # Decrease counter each time
else:
    print("🚀 Event started!")

print("-" * 40)

# ✅ break: exit loop early when condition met
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    user_input = input("Enter your password: ")
    if user_input == "password123":
        # Simulate successful password check
        print("🔓 Access granted.")
        break  # Exit loop immediately
    attempts += 1
    print("❌ Try again.")
else:
    # Runs if 'break' is not encountered
    print("🔒 Too many failed attempts. Access denied.")

print("-" * 40)

# ✅ continue: skip specific iteration
for day in ["Mon", "Tue", "Sun"]:
    if day == "Sun":
        continue  # Skip Sunday
    print(f"Working on {day}")

print("-" * 40)

# ✅ pass statement: acts as a placeholder where code will go later
# It lets you write empty blocks without errors

for i in range(3):
    pass  # No action now, but we plan to add code here later

print("✔️ Used 'pass' to reserve space for future code.")
