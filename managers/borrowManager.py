import os
import json
from models.borrow import Borrow

class BorrowManager:
    """
    Manager class for handling book borrowing records.

    Attributes:
        json_file (str): Path to the JSON file where borrow records are stored.
        borrows (list): List of Borrow objects.
    """
    def __init__(self, json_file="json/borrows.json"):
        """
                Initializes the BorrowManager with the given JSON file path.

                Args:
                    json_file (str, optional): Path to the JSON file. Defaults to "json/borrows.json".
                """
        self.json_file = json_file
        self.borrows = self.load_data()

    def load_data(self):
        """
        Loads borrow data from the JSON file.

        Returns:
            list: A list of Borrow objects.
        """
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r') as file:
            return [Borrow.from_dict(borrow) for borrow in json.load(file)]

    def save_data(self):
        """
        Saves the current borrow data to the JSON file.
        """
        with open(self.json_file, 'w') as file:
            json.dump([borrow.to_dict() for borrow in self.borrows], file, indent=4)

    def add_borrow(self, borrow):
        """
        Adds a new borrow record and saves the updated list to the JSON file.

        Args:
            borrow (Borrow): The borrow record to add.
        """
        self.borrows.append(borrow)
        self.save_data()

    def remove_borrow(self, borrow_id):
        """
        Removes a borrow record by its ID and saves the updated list to the JSON file.

        Args:
            borrow_id (int): The ID of the borrow record to remove.
        """
        self.borrows = [borrow for borrow in self.borrows if borrow.borrow_id != borrow_id]
        self.save_data()

    def update_borrow(self, new_borrow):
        """
         Updates an existing borrow record and saves the updated list to the JSON file.

         Args:
             new_borrow (Borrow): The updated borrow record.
         """
        for i, borrow in enumerate(self.borrows):
            if borrow.borrow_id == new_borrow.borrow_id:
                self.borrows[i] = new_borrow
                self.save_data()
                return

