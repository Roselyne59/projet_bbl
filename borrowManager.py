import os
import json
from borrow import Borrow

class BorrowManager:
    def __init__(self, json_file="json/borrows.json"):
        self.json_file = json_file
        self.borrows = self.load_data()

    def load_data(self):
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r') as file:
            return [Borrow.from_dict(borrow) for borrow in json.load(file)]

    def save_data(self):
        with open(self.json_file, 'w') as file:
            json.dump([borrow.to_dict() for borrow in self.borrows], file, indent=4)

    def add_borrow(self, borrow):
        self.borrows.append(borrow)
        self.save_data()

    def remove_borrow(self, borrow_id):
        self.borrows = [borrow for borrow in self.borrows if borrow.borrow_id != borrow_id]
        self.save_data()

    def update_borrow(self, new_borrow):
        for i, borrow in enumerate(self.borrows):
            if borrow.borrow_id == new_borrow.borrow_id:
                self.borrows[i] = new_borrow
                self.save_data()
                return

    def get_pending_borrows(self):
        return [borrow for borrow in self.borrows if not borrow.is_approved]

    def get_approved_borrows(self):
        return [borrow for borrow in self.borrows if borrow.is_approved]
