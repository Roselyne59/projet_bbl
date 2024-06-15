class Book:
    """
    Class representing a book.

    Attributes:
        book_id (int): The ID of the book.
        title (str): The title of the book.
        authors (str): The authors of the book.
        publication_year (int): The publication year of the book.
        isbn (str): The ISBN of the book.
        editors (list): The editors of the book.
        collections (str): The collection the book belongs to.
        genres (str): The genres of the book.
        is_available (bool): Availability status of the book. Defaults to True.
    """
    book_number = 1

    def __init__(self, book_id,title, authors, publication_year, isbn, editors, collections, genres, is_available = True):
        """
        Initializes a Book object.

        Args:
            book_id (int): The ID of the book.
            title (str): The title of the book.
            authors (str): The authors of the book.
            publication_year (int): The publication year of the book.
            isbn (str): The ISBN of the book.
            editors (list or str): The editors of the book.
            collections (str): The collection the book belongs to.
            genres (str): The genres of the book.
            is_available (bool, optional): Availability status of the book. Defaults to True.
        """
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.publication_year = publication_year
        self.isbn = isbn
        self.editors = editors if isinstance(editors, list) else [editors]
        self.collections = collections
        self.genres = genres
        self.is_available = is_available
        if book_id >= Book.book_number:
            Book.book_number = book_id + 1
    
    def to_dict (self):
        """
        Converts the Book object to a dictionary.

        Returns:
            dict: A dictionary representation of the Book object.
        """
        return{
            "book_id" : self.book_id,
            "titre" : self.title,
            "auteurs" : self.authors,
            "année de publication" : self.publication_year,
            "isbn" : self.isbn,
            "éditeurs" : self.editors,
            "collection" : self.collections,
            "genres" : self.genres,
            "is_available" : self.is_available
        }

    @staticmethod
    def from_dict (data) :
        """
        Creates a Book object from a dictionary.

        Args:
            data (dict): A dictionary containing book data.

        Returns:
            Book: A Book object created from the dictionary data.
        """
        return Book(
            data["book_id"],
            data["titre"],
            data["auteurs"],
            data["année de publication"],
            data["isbn"],
            data.get("éditeurs", ""),
            data["collection"],
            data["genres"],
            data.get("is_available", True)
        )
