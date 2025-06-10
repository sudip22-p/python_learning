# Operator Overloading


# Define a class to represent a point in 2D space
class Point:
    def __init__(self, x, y):
        # Constructor initializes x and y coordinates
        self.x = x
        self.y = y

    def __add__(self, other):
        """
        Operator overloading:
        This special method allows use of + to add two Point objects.
        It adds corresponding x and y values and returns a new Point.
        """
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        """
        String representation:
        When print() is called on a Point object, this method defines
        what gets displayed.
        """
        return f"({self.x}, {self.y})"


# Create two Point objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Add the two points using the overloaded + operator
result = p1 + p2  # Internally calls: p1.__add__(p2)

# Print the result using the custom __str__ method
print(result)  # Output: (4, 6)

"""

Explanation:
__add__ and __str__ are special methods (also called dunder methods or magic methods) that Python calls automatically when you use certain built-in syntax.
`__add__` allows you to define how the + operator behaves for your class.
`__str__` defines how the object should be represented as a string, which is useful for printing.
some more examples of operator overloading include:
_sub__ for -
__mul__ for *
__eq__ for ==
__lt__ for <, etc.


# Operator overloading meaning:
# Operator overloading allows you to define custom behavior for built-in operators (like +, -, *, etc.) when they are used with instances of your class.
The + operator already exists (it works for numbers).
You are "loading more meaning" onto that same operator — now it also works for your class.
in simple terms, operator overloading allows you to define how operators like +, -, *, etc. behave when applied to instances of your class.
"""
