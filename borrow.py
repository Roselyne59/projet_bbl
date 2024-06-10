class Borrow:
    def __init__(self, borrow_id, user_id, book_id, start_date, return_date, is_approved=False):
        self.borrow_id = borrow_id
        self.user_id = user_id
        self.book_id = book_id
        self.start_date = start_date
        self.due_date = return_date
        self.is_approved = is_approved

    def to_dict(self):
        return {
            "borrow_id": self.borrow_id,
            "user_id": self.user_id,
            "book_id": self.book_id,
            "start_date": self.start_date,
            "due_date": self.due_date,
            "is_approved": self.is_approved
        }

    @staticmethod
    def from_dict(data):
        return Borrow(
            data["borrow_id"],
            data["user_id"],
            data["book_id"],
            data["start_date"],
            data["due_date"],
            data.get("is_approved", False)
        )


