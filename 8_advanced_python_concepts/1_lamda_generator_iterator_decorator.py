# Lambda Functions (Quick One-Line Functions)

# Think of lambda like a mini calculator that you define in one line
# You don't need to give it a name like regular functions

add = lambda x, y: x + y  # adds two numbers
print("➕ Lambda Add:", add(2, 3))  # Output: 5


# Generator Function (Produces items one by one — like a vending machine)

# Instead of returning all items at once (which can be memory heavy),
# 'yield' gives one item at a time, and remembers where it left off


def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # pause and wait to be called again
        count += 1


print("🔁 Generator Output (like vending items):")
for num in count_up_to(3):
    print(num)  # Prints 1, then 2, then 3 — one at a time


# Iterator (You manually take out items one by one)

# Like taking cookies out of a jar using a tool (the iterator)
my_list = [10, 20, 30]
iterator = iter(my_list)  # Get an iterator (tool) from the list

print("🔄 Manual Iterator:")
print(next(iterator))  # Grabs 10
print(next(iterator))  # Grabs 20
print(next(iterator))  # Grabs 30
# If you try next again, there’s no cookie left = StopIteration error


# Decorator (Adds extra feature to a function — like wrapping a gift 🎁)


# Imagine decorating a function by wrapping it with extra code
def greet_decorator(func):
    def wrapper():
        print("👋 Before the function runs")  # Like opening the gift
        func()  # Actual function
        print("👋 After the function runs")  # Like saying thank you after unwrapping

    return wrapper


# Original function (our gift)
@greet_decorator  # We decorate it with extra behavior
def say_hello():
    print("Hello from inside function!")


say_hello()

# Output:
# 👋 Before the function runs
# Hello from inside function!
# 👋 After the function runs
