import json
import os
from book import Book

class BookService:
    def __init__(self, json_file="books.json") :
        self.json_file = json_file
        self.books = self.load_books()

    def load_books(self) :
        if not os.path.exists(self.json_file):
            return[]
        with open(self.json_file, 'r') as file:
            books_data = json.load(file)
            books = []
            for book_data in books_data:
                book = Book(
                    title=book_data.get("title", ""),
                    authors=book_data.get("authors", []),
                    publication_year=book_data.get("publication_year", 0),
                    isbn=book_data.get("isbn", ""),
                    editor=book_data.get("editor", ""),
                    genders=book_data.get("genders", [])
                )
                book.id = book_data.get("book_id")
                books.append(book)
            return books
        
    def save_books(self):
        books_data = []
        for book in self.books:
            book_data = {
                "book_id": book.id,
                "title": book.title,
                "authors": book.authors,
                "publication_year": book.publication_year,
                "isbn": book.isbn,
                "editor": book.editor,
                "genders": book.genders
            }
            books_data.append(book_data)
        with open(self.json_file, 'w') as file:
            json.dump(books_data, file, indent=4)

    def add_book(self, book) :
        self.books.append(book)
        self.save_books()

    def remove_book(self, book):
        self.books.remove(book)
        self.save_books()