from book_store import BookStore

def search_book():
    store = BookStore()
    keyword = input("Enter title, author, or ISBN to search: ")
    store.search_book(keyword)