import os
import json
from models.borrow import Borrow

class BorrowManager:
    """_summary_
    """
    def __init__(self, json_file="json/borrows.json"):
        """_summary_

        Args:
            json_file (str, optional): _description_. Defaults to "json/borrows.json".
        """
        self.json_file = json_file
        self.borrows = self.load_data()

    def load_data(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r') as file:
            return [Borrow.from_dict(borrow) for borrow in json.load(file)]

    def save_data(self):
        """_summary_
        """
        with open(self.json_file, 'w') as file:
            json.dump([borrow.to_dict() for borrow in self.borrows], file, indent=4)

    def add_borrow(self, borrow):
        """_summary_

        Args:
            borrow (_type_): _description_
        """
        self.borrows.append(borrow)
        self.save_data()

    def remove_borrow(self, borrow_id):
        """_summary_

        Args:
            borrow_id (_type_): _description_
        """
        self.borrows = [borrow for borrow in self.borrows if borrow.borrow_id != borrow_id]
        self.save_data()

    def update_borrow(self, new_borrow):
        """_summary_

        Args:
            new_borrow (_type_): _description_
        """
        for i, borrow in enumerate(self.borrows):
            if borrow.borrow_id == new_borrow.borrow_id:
                self.borrows[i] = new_borrow
                self.save_data()
                return

