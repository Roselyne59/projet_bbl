from book import Book

class Shelf :
    shelf_number = 1
    
    def __init__(self, shelf_id, number, letter, books=None) :
        self.shelf_id = shelf_id
        self.number = number
        self.letter = letter
        self.books = books if books is not None else []
        if shelf_id >= Shelf.shelf_number :
            Shelf.shelf_number = shelf_id + 1

    def __str__(self) :
        return f"{self.number}{self.letter}"
    
    def to_dict(self) :
        return{
            "shelf_id" : self.shelf_id,
            "number" : self.number,
            "letter" : self.letter,
            "books" : [book.to_dict() for book in self.books]
        }
    
    @staticmethod
    def from_dict(data) :
        books = [Book.from_dict(book_data) for book_data in data.get("books", [])]
        return Shelf(
            data["shelf_id"],
            data["number"],
            data["letter"],
            books
        )