import json
import os
from models.book import Book

class BookManager:
    """
    Manager class for handling book records.

    Attributes:
        books_json (str): Path to the JSON file where book records are stored.
        editors_json (str): Path to the JSON file where editor records are stored.
        collections_json (str): Path to the JSON file where collection records are stored.
        genres_json (str): Path to the JSON file where genre records are stored.
        books (list): List of Book objects.
        editors (list): List of editors.
        collections (list): List of collections.
        genres (list): List of genres.
    """
    def __init__(self, books_json="json/books.json", editors_json="json/editors.json", collections_json="json/collections.json", genres_json="json/genres.json"):
        """
        Initializes the BookManager with the given JSON file paths.

        Args:
            books_json (str, optional): Path to the JSON file for books. Defaults to "json/books.json".
            editors_json (str, optional): Path to the JSON file for editors. Defaults to "json/editors.json".
            collections_json (str, optional): Path to the JSON file for collections. Defaults to "json/collections.json".
            genres_json (str, optional): Path to the JSON file for genres. Defaults to "json/genres.json".
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
        """
        Loads book data from the JSON file.

        Returns:
            list: A list of Book objects.
        """
        if not os.path.exists(self.books_json):
            return []
        with open(self.books_json, 'r', encoding='utf-8') as file:
            books_data = json.load(file)
            return [Book.from_dict(book_data) for book_data in books_data]

    def save_books(self):
        """
        Saves the current book data to the JSON file.
        """
        with open(self.books_json, 'w', encoding='utf-8') as file:
            books_data = [book.to_dict() for book in self.books]
            json.dump(books_data, file, ensure_ascii=False, indent=4)

    def add_book(self, book):
        """
        Adds a new book record and saves the updated list to the JSON file.

        Args:
            book (Book): The book record to add.
        """
        self.books.append(book)
        self.save_books()

    def update_book(self, book):
        """
        Updates an existing book record and saves the updated list to the JSON file.

        Args:
            book (Book): The updated book record.

        Raises:
            ValueError: If the book is not found.
        """
        for i, b in enumerate(self.books):
            if b.book_id == book.book_id:
                self.books[i] = book
                self.save_books()
                return
        raise ValueError("Book not found")

    def remove_book(self, book_id):
        """
        Removes a book record by its ID and saves the updated list to the JSON file.

        Args:
            book_id (int): The ID of the book record to remove.
        """
        self.books = [book for book in self.books if book.book_id != book_id]
        self.save_books()

    def load_editors(self):
        """
        Loads editor data from the JSON file.

        Returns:
            list: A list of editors.
        """
        if not os.path.exists(self.editors_json) :
            return []
        with open(self.editors_json, 'r', encoding='utf-8') as file:
            return json.load(file)
        
    def load_collections(self):
        """
        Loads collection data from the JSON file.

        Returns:
            list: A list of collections.
        """
        if not os.path.exists(self.collections_json) :
            return []
        with open(self.collections_json, 'r', encoding='utf-8') as file:
            return json.load(file)

    def load_genres(self):
        """
        Loads genre data from the JSON file.

        Returns:
            list: A list of genres.
        """
        if not os.path.exists(self.genres_json) :
            return []
        with open(self.genres_json, 'r', encoding='utf-8') as file:
            return json.load(file)

    def get_book_id_by_title(self, title):
        """
        Retrieves the book ID by its title.

        Args:
            title (str): The title of the book.

        Returns:
            int: The ID of the book, or None if not found.
        """
        for book in self.books:
            if book.title == title:
                return book.book_id
        return None

    def get_book_title_by_id(self, book_id):
        """
        Retrieves the book title by its ID.

        Args:
            book_id (int): The ID of the book.

        Returns:
            str: The title of the book, or "Unknown Title" if not found.
        """
        for book in self.books:
            if book.book_id == book_id:
                return book.title
        return "Unknown Title"
    