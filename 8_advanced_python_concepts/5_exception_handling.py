# ✅ Exception Handling in Python
# Used to gracefully handle runtime errors without crashing the program

try:
    num = int(input("Enter a number: "))
    result = 100 / num  # May raise ZeroDivisionError
    print("✅ Result:", result)
except ZeroDivisionError:
    print("❌ You can't divide by zero!")
except ValueError:
    print("❌ Please enter a valid number!")
except Exception as e:
    # Generic exception (catches any error not specifically handled)
    print(f"⚠️ An unexpected error occurred: {e}")
finally:
    print("🔚 This runs no matter what (cleanup, closing files, etc.)")


# ✅ Custom Exception Example
# You can define your own error types using class and raise


class TooSmallError(Exception):
    """Custom exception when value is too small"""

    pass


def check_age(age):
    if age < 18:
        raise TooSmallError("Age must be at least 18 to register.")
    print("✅ Registration successful.")


try:
    user_age = int(input("Enter your age: "))
    check_age(user_age)
except TooSmallError as e:
    print("🚫 Custom Error:", e)
except ValueError:
    print("❌ Invalid age format.")

"""
💡 Real-World Example:
- try-except = like wearing a helmet when riding a bike: prevents damage on error.
- finally = like putting your bike in the garage after riding, no matter what happened.
- custom error = like raising your own alert if someone breaks your house rules.
"""
