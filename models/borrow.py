class Borrow:
    """_summary_
    """
    def __init__(self, borrow_id, user_id, user_name,book_id, book_title,start_date, return_date):
        """_summary_

        Args:
            borrow_id (_type_): _description_
            user_id (_type_): _description_
            user_name (_type_): _description_
            book_id (_type_): _description_
            book_title (_type_): _description_
            start_date (_type_): _description_
            return_date (_type_): _description_
        """
        self.borrow_id = borrow_id
        self.user_id = user_id
        self.user_name = user_name
        self.book_id = book_id
        self.book_title = book_title
        self.start_date = start_date
        self.due_date = return_date
       
    def to_dict(self):
        """_summary_

        Returns:
            _type_: _description_
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
        """_summary_

        Args:
            data (_type_): _description_

        Returns:
            _type_: _description_
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


