# ✅ Basic Function with parameters and return
def greet(name):
    """Greets the user by name."""  # docstring
    return f"Hello, {name}!"


print(greet("Sud"))


# ✅ Function with default argument
def add(a, b=5):
    return a + b


print(add(3))  # 3 + 5 = 8
print(add(3, 2))  # 3 + 2 = 5

# ✅ Lambda (anonymous) function is a small function without a name used for short operations like sorting or filtering
square = lambda x: x * x
print(square(4))  # 16

# ✅ Variable scope
x = 10  # global


def show_scope():
    x = 5  # local
    print("Inside function:", x)


show_scope()
print("Outside function:", x)
