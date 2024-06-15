import json
import os
from book import Book

class BookManager:
    def __init__(self, books_json="json/books.json", editors_json="json/editors.json", collections_json="json/collections.json", genres_json="json/genres.json"):
        self.books_json = books_json
        self.editors_json = editors_json
        self.collections_json = collections_json
        self.genres_json = genres_json
        self.books = self.load_books()
        self.editors = self.load_editors()
        self.collections = self.load_collections()
        self.genres = self.load_genres()

    def load_books(self):
        if not os.path.exists(self.books_json):
            return []
        with open(self.books_json, 'r', encoding='utf-8') as file:
            books_data = json.load(file)
            return [Book.from_dict(book_data) for book_data in books_data]

    def save_books(self):
        with open(self.books_json, 'w', encoding='utf-8') as file:
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

    def load_editors(self):
        if not os.path.exists(self.editors_json) :
            return []
        with open(self.editors_json, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    def load_collections(self):
        if not os.path.exists(self.collections_json) :
            return []
        with open(self.collections_json, 'r', encoding='utf-8') as file:
            return json.load(file)

    def load_genres(self):
        if not os.path.exists(self.genres_json) :
            return []
        with open(self.genres_json, 'r', encoding='utf-8') as file:
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
    