from models.book import Book

class Shelf :
    """
    Class representing a shelf.

    Attributes:
        shelf_id (int): The ID of the shelf.
        number (int): The number of the shelf.
        letter (str): The letter of the shelf.
        books (list): List of Book objects on the shelf.
    """
    shelf_number = 1
    
    def __init__(self, shelf_id, number, letter) :
        """
        Initializes a Shelf object.

        Args:
            shelf_id (int): The ID of the shelf.
            number (int): The number of the shelf.
            letter (str): The letter of the shelf.
        """
        self.shelf_id = shelf_id
        self.number = number
        self.letter = letter
        self.books = []
        if shelf_id >= Shelf.shelf_number :
            Shelf.shelf_number = shelf_id + 1

    def __str__(self) :
        """
        Returns a string representation of the shelf.

        Returns:
            str: The string representation of the shelf.
        """
        return f"{self.number}{self.letter}"
    
    def to_dict(self) :
        """
        Converts the Shelf object to a dictionary.

        Returns:
            dict: A dictionary representation of the Shelf object.
        """
        return{
            "shelf_id" : self.shelf_id,
            "number" : self.number,
            "letter" : self.letter,
            "books" : [book.to_dict() for book in self.books]
        }
    
    @staticmethod
    def from_dict(data) :
        """
        Creates a Shelf object from a dictionary.

        Args:
            data (dict): A dictionary containing shelf data.

        Returns:
            Shelf: A Shelf object created from the dictionary data.
        """
        shelf = Shelf(data["shelf_id"], data["number"], data["letter"])
        shelf.books = [Book.from_dict(book) for book in data.get("books", [])]
        return shelf