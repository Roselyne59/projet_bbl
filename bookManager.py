import json
import os
from book import Book

class BookManager:
    def __init__(self, json_file="json/books.json"):
        self.json_file = json_file
        self.books = self.load_books()
        self.next_id = self.get_next_id()

    def load_books(self):
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r') as file:
            return [Book.from_dict(book) for book in json.load(file)]

    def save_books(self):
        with open(self.json_file, 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def load_genres(self):
        json_file = os.path.join(os.path.dirname(__file__), 'json', 'genres.json')
        with open(json_file, 'r') as file :
            self.genres_data = json_file((file))

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def remove_book(self, book_id):
        self.books = [b for b in self.books if b.book_id != book_id]
        self.save_books()

    def update_user(self, edit_book):
        for i, book in enumerate(self.books):
            if book.book_id == edit_book.book_id:
                self.books[i] = edit_book
                self.save_books()
                return

#    def find_book_by_title(self, title):
#        return next((book for book in self.books if book.title == title), None)

    
