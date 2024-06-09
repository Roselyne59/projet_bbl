import json
import os
from book import Book

class Wishlist:
    def __init__(self, json_file="json/wishlist.json") :
        self.json_file = json_file
        self.books = self.load_books()

    def load_books(self):
        if not os.path.exists(self.json_file):
            return[]
        with open(self.json_file, 'r') as file:
            return [Book.from_dict(book) for book in json.load(file)]
        
    def save_books(self):
        with open(self.json_file, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    
    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, book_id):
        self.books = [b for b in self.books if b.book_id != book_id]
        self.save_books()