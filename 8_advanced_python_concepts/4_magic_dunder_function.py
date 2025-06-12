# Magic/Dunder Methods (also called special methods)
# These are special methods in Python that start and end with double underscores (__)


class Book:
    def __init__(self, title, author, pages):
        # __init__ is called when a new object is created
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        # __str__ defines what print(book) will show
        return f"📘 {self.title} by {self.author}"

    def __len__(self):
        # __len__ defines what len(book) will return
        return self.pages

    def __eq__(self, other):
        # __eq__ is used to compare two objects using ==
        return self.pages == other.pages


# Create two Book objects
book1 = Book("Python 101", "Alice", 300)
book2 = Book("Learn Python", "Bob", 300)
book3 = Book("Short Guide", "Eve", 150)

# Print book info (calls __str__)
print(book1)  # Output: 📘 Python 101 by Alice

# Get number of pages (calls __len__)
print("📄 Pages in book1:", len(book1))  # Output: 300

# Compare two books (calls __eq__)
print("📚 book1 == book2?", book1 == book2)  # True
print("📚 book1 == book3?", book1 == book3)  # False

"""
🔍 Real-world analogy:
- __str__ = how the object looks when printed, like a label on a box.
- __len__ = how many pages the book has, like checking its weight.
- __eq__ = comparing if two books are of same size.

You can also override:
- __add__ to use + operator on objects
- __lt__, __gt__ for <, >
- __getitem__ to make your object indexable like a list
"""
