class Borrow:
    """
    Class representing a book borrowing record.

    Attributes:
        borrow_id (int): The ID of the borrow record.
        user_id (int): The ID of the user who borrowed the book.
        user_name (str): The name of the user who borrowed the book.
        book_id (int): The ID of the borrowed book.
        book_title (str): The title of the borrowed book.
        start_date (str): The start date of the borrowing period.
        due_date (str): The due date for returning the book.
    """
    def __init__(self, borrow_id, user_id, user_name,book_id, book_title,start_date, return_date):
        """
        Initializes a Borrow object.

        Args:
            borrow_id (int): The ID of the borrow record.
            user_id (int): The ID of the user who borrowed the book.
            user_name (str): The name of the user who borrowed the book.
            book_id (int): The ID of the borrowed book.
            book_title (str): The title of the borrowed book.
            start_date (str): The start date of the borrowing period.
            return_date (str): The due date for returning the book.
        """
        self.borrow_id = borrow_id
        self.user_id = user_id
        self.user_name = user_name
        self.book_id = book_id
        self.book_title = book_title
        self.start_date = start_date
        self.due_date = return_date
       
    def to_dict(self):
        """
        Converts the Borrow object to a dictionary.

        Returns:
            dict: A dictionary representation of the Borrow object.
        """
        return {
            "borrow_id": self.borrow_id,                
            "user_id": self.user_id,
            "user_name": self.user_name,
            "book_id": self.book_id,
            "book_title": self.book_title,
            "start_date": self.start_date,
            "due_date": self.due_date,

        }

    @staticmethod
    def from_dict(data):
        """
        Creates a Borrow object from a dictionary.

        Args:
            data (dict): A dictionary containing borrow record data.

        Returns:
            Borrow: A Borrow object created from the dictionary data.
        """
        return Borrow(
            data["borrow_id"],
            data["user_id"],
            data["user_name"],
            data["book_id"],
            data["book_title"],
            data["start_date"],
            data["due_date"],
        )


