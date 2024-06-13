import json
import os
from book import Book

class BookManager:
    def __init__(self, json_file="json/books.json"):
        self.json_file = json_file
        self.books = self.load_books()
        self.genres = self.load_genres()

    def load_books(self):
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r', encoding='utf-8') as file:
            books_data = json.load(file)
            return [Book.from_dict(book_data) for book_data in books_data]

    def save_books(self):
        with open(self.json_file, 'w', encoding='utf-8') as file:
            books_data = [book.to_dict() for book in self.books]
            json.dump(books_data, file, ensure_ascii=False, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()

    def update_book(self, book):
        for i, b in enumerate(self.books):
            if b.book_id == book.book_id:
                self.books[i] = book
                self.save_books()
                return
        raise ValueError("Book not found")

    def remove_book(self, book_id):
        self.books = [book for book in self.books if book.book_id != book_id]
        self.save_books()

    def load_genres(self):
        with open('json/genres.json', 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_book_id_by_title(self, title):
        for book in self.books:
            if book.title == title:
                return book.book_id
        return None

    def get_book_title_by_id(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book.title
        return "Unknown Title"
    
