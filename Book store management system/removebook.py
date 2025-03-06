from book_store import BookStore

def remove_book():
    store = BookStore()
    isbn = input("Enter ISBN of book to remove: ")
    store.remove_book(isbn)