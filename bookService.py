
import json
import os
from book import Book

class BookService:
    def __init__(self, json_file="json/books.json"):
        self.json_file = json_file
        self.books = self.load_books()
        self.next_id = self.get_next_id()

    def load_books(self):
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r') as file:
            books_data = json.load(file)
            return [Book(**data) for data in books_data]

    def save_books(self):
        books_data = [{**vars(book), "id": book.id} for book in self.books]
        with open(self.json_file, 'w') as file:
            json.dump(books_data, file, indent=4)

    def add_book(self, book):
        if book.id is None:
            book.id = self.next_id
            self.next_id += 1
        self.books.append(book)
        self.save_books()

    def remove_book(self, book):
        self.books = [b for b in self.books if b.id != book.id]
        self.save_books()

    def find_book_by_title(self, title):
        return next((book for book in self.books if book.title == title), None)

    def get_next_id(self):
        if not self.books:
            return 0
        max_id = max(book.id for book in self.books)
        return max_id + 1
