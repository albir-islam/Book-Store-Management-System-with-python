from addbook import add_book
from viewbook import view_books
from searchbook import search_book
from removebook import remove_book

def main():
    while True:
        print("\nBook Store Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            remove_book()
        elif choice == "5":
            print("Data saved.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()