from models.book import Book

class Shelf :
    """_summary_

    Returns:
        _type_: _description_
    """
    shelf_number = 1
    
    def __init__(self, shelf_id, number, letter) :
        """_summary_

        Args:
            shelf_id (_type_): _description_
            number (_type_): _description_
            letter (_type_): _description_
        """
        self.shelf_id = shelf_id
        self.number = number
        self.letter = letter
        self.books = []
        if shelf_id >= Shelf.shelf_number :
            Shelf.shelf_number = shelf_id + 1

    def __str__(self) :
        """_summary_

        Returns:
            _type_: _description_
        """
        return f"{self.number}{self.letter}"
    
    def to_dict(self) :
        """_summary_
        """
        return{
            "shelf_id" : self.shelf_id,
            "number" : self.number,
            "letter" : self.letter,
            "books" : [book.to_dict() for book in self.books]
        }
    
    @staticmethod
    def from_dict(data) :
        """_summary_

        Args:
            data (_type_): _description_

        Returns:
            _type_: _description_
        """
        shelf = Shelf(data["shelf_id"], data["number"], data["letter"])
        shelf.books = [Book.from_dict(book) for book in data.get("books", [])]
        return shelf