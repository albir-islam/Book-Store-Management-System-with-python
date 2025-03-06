class Book:
    def __init__(self, title, author, isbn, genre, price, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.price = price
        self.quantity = quantity

    def dict(self):
        return{
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "genre": self.genre,
            "price": self.price,
            "quantity": self.quantity
        }
