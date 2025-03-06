from book_store import BookStore
from book import Book


def add_book():
    store = BookStore()

    title = input("Enter book title: ")
    if not isinstance(title, str) or title.strip() == "":
        print("Error: The book title must be a string.")
        return

    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    genre = input("Enter book genre: ")

    try:
        price = float(input("Enter book price: "))
        quantity = int(input("Enter book quantity: "))
        if price <= 0 or quantity < 0:
            raise ValueError
        new_book = Book(title, author, isbn, genre, price, quantity)
        store.add_book(new_book)
    except ValueError:
        print("Error: Price must be a positive number and quantity must be a non-negative integer.")