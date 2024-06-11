import json
import os
from shelf import Shelf

class ShelfManager:
    def __init__(self, json_file="json/shelves.json"):
        self.json_file = json_file
        self.shelves = self.load_shelves()

    def load_shelves(self):
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r', encoding='utf-8') as file:
            shelves_data = json.load(file)
            return [Shelf.from_dict(data) for data in shelves_data]

    def save_shelves(self):
        with open(self.json_file, 'w', encoding='utf-8') as file:
            json.dump([shelf.to_dict() for shelf in self.shelves], file, ensure_ascii=False, indent=4)
        
    def add_shelf(self, shelf):
        self.shelves.append(shelf)
        self.save_shelves()

    def update_shelf(self, shelf_number, new_shelf):
        for i, s in enumerate(self.shelves):
            if s.number == shelf_number :
                self.shelves[i] = new_shelf
                self.save_shelves()
                return
        raise ValueError("Etagère introuvable...")

    def remove_shelf(self, shelf_number):
        self.shelves = [shelf for shelf in self.shelves if shelf.number != shelf_number]
        self.save_shelves()

    def add_book_to_shelf(self, shelf_number, book):
        for shelf in self.shelves:
            if shelf.number == shelf_number:
                shelf.books.append(book.to_dict())
                self.save_shelves()
                return
        raise ValueError("Etagère introuvable...")

    def remove_book_from_shelf(self, shelf_number, book_id):
        for shelf in self.shelves:
            if shelf.number == shelf_number :
                shelf.books = [book for book in shelf.books if book["book_id"] != book_id]
                self.save_shelves()
                return
        raise ValueError("Etagère introuvable...")