
# 📌 Example 1: Age-based message using if-elif-else
age = int(input("Enter your age: "))

if age < 13:
    print("You're a child.")
elif age < 20: #elif = else if
    print("You're a teenager.")
elif age < 60: #below : showing multiple line inside block managed by indentation
    print("You're an adult.")
    print("Enjoy your life!")
else:
    print("You're a senior citizen.")

# 📌 Example 2: Login role check using match-case (Python 3.10+)
# Note: Works only on Python 3.10 and above
role = input("Enter your role (admin/user/guest): ").lower()

match role: #python has match case instead of switch case
    case "admin":
        print("Redirecting to admin dashboard...")
    case "user":
        print("Redirecting to user homepage...")
    case "guest":
        print("Redirecting to guest view...")
    case _:
        print("Invalid role entered.")

# ✅ Summary:
# - if-elif-else is used for conditional branching
# - match-case is similar to switch-case in other languages (used for clean multi-checks)
