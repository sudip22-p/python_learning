def greet():
    print("Hello from greet function!")


def add(a, b):
    return a - b


# This block runs only when the file is run directly
if __name__ == "__main__":  # this line checks if the script is being run directly
    # If true, it means the script is being run directly, not imported
    # if imported, this block will not execute
    print("Running directly...")
    greet()
    print("Sum is:", add(9, 4))
