"""
Advanced Data Structures in Python
- Complex nested dicts and lists combined
- Nested comprehensions [Comprehensions in Python are a concise way to create new lists, sets, or dictionaries by iterating over an existing iterable (like a list or range) and optionally filtering elements.]
- Using collections.Counter & defaultdict in real scenarios
- Practical example: Inventory management for a bookstore

"""

from collections import defaultdict, Counter

# Complex nested structure: Inventory of a bookstore
# Each genre has books, each book has multiple copies with status (sold/in stock)
bookstore = {
    "Science Fiction": [
        {
            "title": "Dune",
            "authors": ["Frank Herbert"],
            "copies": [{"id": 1, "status": "in_stock"}, {"id": 2, "status": "sold"}],
        },
        {
            "title": "Neuromancer",
            "authors": ["William Gibson"],
            "copies": [{"id": 3, "status": "in_stock"}],
        },
    ],
    "Fantasy": [
        {
            "title": "The Hobbit",
            "authors": ["J.R.R. Tolkien"],
            "copies": [{"id": 4, "status": "sold"}, {"id": 5, "status": "in_stock"}],
        },
        {
            "title": "Harry Potter",
            "authors": ["J.K. Rowling"],
            "copies": [{"id": 6, "status": "in_stock"}],
        },
    ],
}

# Nested comprehension: Get all book titles with available copies
available_books = [
    book["title"]
    for genre_books in bookstore.values()
    for book in genre_books
    if any(copy["status"] == "in_stock" for copy in book["copies"])
]

print("Available books:", available_books)

# Use defaultdict and Counter together to count sold vs in_stock per genre
genre_status_count = defaultdict(Counter)

for genre, books in bookstore.items():
    for book in books:
        for copy in book["copies"]:
            genre_status_count[genre][copy["status"]] += 1

print("\nSold vs In-stock count per genre:")
for genre, counts in genre_status_count.items():
    print(f"{genre}: {dict(counts)}")

# Access deeply nested data: List all authors for Fantasy genre
fantasy_authors = {
    author for book in bookstore["Fantasy"] for author in book["authors"]
}
print("\nFantasy genre authors:", fantasy_authors)

# Update nested data: Mark all copies of "Dune" as sold
for book in bookstore["Science Fiction"]:
    if book["title"] == "Dune":
        for copy in book["copies"]:
            copy["status"] = "sold"

print("\nAfter selling all Dune copies:")
print(bookstore["Science Fiction"][0])  # Show updated Dune book copies

# Real-world use case: check if any genre is completely sold out (no in_stock copies)
sold_out_genres = [
    genre for genre, counts in genre_status_count.items() if counts["in_stock"] == 0
]
print("\nSold out genres:", sold_out_genres)
