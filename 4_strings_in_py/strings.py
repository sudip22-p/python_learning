# 📌 4. Strings in Python

# ✅ Basic string usage
name = "Sud"
greeting = "Hello, " + name  # Concatenation
print(greeting)

# ✅ String indexing (0-based)
print(name[0])  # S
print(name[-1])  # d (last character)

# ✅ String slicing
print(name[2:3])  # d (index 2 to 3)
print(name[:2])  # Su
print(name[2:])  # d

# ✅ Common string methods
msg = "  python is FUN  "
print(msg.strip())  # remove spaces from both sides
print(msg.upper())  # PYTHON IS FUN
print(msg.lower())  # python is fun
print(msg.replace("FUN", "awesome"))  # python is awesome
print("python" in msg)  # True (membership check)

# ✅ String formatting
age = 22
print("My name is {} and I am {} years old.".format(name, age))  # classic style

# ✅ f-strings (clean & modern way)
print(f"My name is {name} and I am {age} years old.")  # recommended
