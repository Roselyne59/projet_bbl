import json
import os
from models.book import Book

class BookManager:
    """_summary_
    """
    def __init__(self, books_json="json/books.json", editors_json="json/editors.json", collections_json="json/collections.json", genres_json="json/genres.json"):
        """_summary_

        Args:
            books_json (str, optional): _description_. Defaults to "json/books.json".
            editors_json (str, optional): _description_. Defaults to "json/editors.json".
            collections_json (str, optional): _description_. Defaults to "json/collections.json".
            genres_json (str, optional): _description_. Defaults to "json/genres.json".
        """
        self.books_json = books_json
        self.editors_json = editors_json
        self.collections_json = collections_json
        self.genres_json = genres_json
        self.books = self.load_books()
        self.editors = self.load_editors()
        self.collections = self.load_collections()
        self.genres = self.load_genres()

    def load_books(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if not os.path.exists(self.books_json):
            return []
        with open(self.books_json, 'r', encoding='utf-8') as file:
            books_data = json.load(file)
            return [Book.from_dict(book_data) for book_data in books_data]

    def save_books(self):
        """_summary_
        """
        with open(self.books_json, 'w', encoding='utf-8') as file:
            books_data = [book.to_dict() for book in self.books]
            json.dump(books_data, file, ensure_ascii=False, indent=4)

    def add_book(self, book):
        """_summary_

        Args:
            book (_type_): _description_
        """
        self.books.append(book)
        self.save_books()

    def update_book(self, book):
        """_summary_

        Args:
            book (_type_): _description_

        Raises:
            ValueError: _description_
        """
        for i, b in enumerate(self.books):
            if b.book_id == book.book_id:
                self.books[i] = book
                self.save_books()
                return
        raise ValueError("Book not found")

    def remove_book(self, book_id):
        """_summary_

        Args:
            book_id (_type_): _description_
        """
        self.books = [book for book in self.books if book.book_id != book_id]
        self.save_books()

    def load_editors(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if not os.path.exists(self.editors_json) :
            return []
        with open(self.editors_json, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    def load_collections(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if not os.path.exists(self.collections_json) :
            return []
        with open(self.collections_json, 'r', encoding='utf-8') as file:
            return json.load(file)

    def load_genres(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if not os.path.exists(self.genres_json) :
            return []
        with open(self.genres_json, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_book_id_by_title(self, title):
        """_summary_

        Args:
            title (_type_): _description_

        Returns:
            _type_: _description_
        """
        for book in self.books:
            if book.title == title:
                return book.book_id
        return None

    def get_book_title_by_id(self, book_id):
        """_summary_

        Args:
            book_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        for book in self.books:
            if book.book_id == book_id:
                return book.title
        return "Unknown Title"
    