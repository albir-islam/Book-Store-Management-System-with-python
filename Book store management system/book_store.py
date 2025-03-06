from book import Book
import bookdata

class BookStore:
    def __init__(self):
        self.books = bookdata.load_books()

    def add_book(self, book):
        for i in self.books:
            if i["isbn"] == book.isbn:
                print("Error! Same book exists.")
                return

        self.books.append(book.dict())
        bookdata.save_books(self.books)
        print("Successfully added a book.")

    def view_book(self):
        if not self.books:
            print("No books available.")
            return
        print("\n----- Book List -----")
        for book in self.books:
            print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, "
                  f"Genre: {book['genre']}, Price: {book['price']}, Stock: {book['quantity']}")


    def search_book(self, keyword):
        results = [book for book in self.books if keyword.lower() in book['title'].lower()
                   or keyword.lower() in book['author'].lower() or keyword == book['isbn']]
        if results:
            print("\n----- Search Results -----")
            for book in results:
                print(f"Title: {book['title']}, Author: {book['author']}, ISBN: {book['isbn']}, "
                      f"Genre: {book['genre']}, Price: ${book['price']}, Stock: {book['quantity']}")
        else:
            print("No books found matching the search.")

    def remove_book(self, isbn):

        if any(book["isbn"] == isbn for book in self.books):
            self.books = [book for book in self.books if book["isbn"] != isbn]
            bookdata.save_books(self.books)
            print("Book removed successfully!")
        else:
            print("Error: No book found with the given ISBN.")

    