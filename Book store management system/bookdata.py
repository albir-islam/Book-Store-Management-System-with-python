import json

filename = "book_store.json"

def load_books():
    try:
        with open(filename, 'r') as fp:
            return json.load(fp)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]

def save_books(books):
    with open(filename, 'w') as fp:
         return json.dump(books, fp, indent=4)
