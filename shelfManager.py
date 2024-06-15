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
        if self.is_duplicate(shelf.number, shelf.letter):
            raise ValueError("Une étagère avec cette combinaison existe déjà !")
        self.shelves.append(shelf)
        self.save_shelves()

    def update_shelf(self, old_number, new_shelf):
        for i, s in enumerate(self.shelves):
            if s.number == old_number:
                if (new_shelf.number != old_number or new_shelf.letter != s.letter) and self.is_duplicate(new_shelf.number, new_shelf.letter):
                    raise ValueError("Une étagère avec cette combinaison existe déjà !")
                self.shelves[i] = new_shelf
                self.save_shelves()
                return
        raise ValueError("Etagère introuvable...")

    def remove_shelf(self, shelf_id):
        self.shelves = [shelf for shelf in self.shelves if shelf.shelf_id != shelf_id]
        self.update_shelf_ids()
        self.save_shelves()
        
    def update_shelf_ids(self):
        for i, shelf in enumerate(self.shelves):
            shelf.shelf_id = i + 1
        Shelf.shelf_number = len(self.shelves) + 1

    def add_book_to_shelf(self, shelf_number, book):
        if self.is_book_in_any_shelf(book.book_id):
            raise ValueError("Ce livre est déjà dans une autre étagère.")
        for shelf in self.shelves:
            if shelf.number == shelf_number:
                shelf.books.append(book)
                self.save_shelves()
                return
        raise ValueError("Etagère introuvable...")

    def remove_book_from_shelf(self, shelf_number, book_id):
        for shelf in self.shelves:
            if shelf.number == shelf_number:
                shelf.books = [book for book in shelf.books if book.book_id != book_id]
                self.save_shelves()
                return
        raise ValueError("Etagère introuvable...")
    
    def is_duplicate(self, number, letter):
        return any(shelf.number == number and shelf.letter == letter for shelf in self.shelves)
    
    def is_book_in_any_shelf(self, book_id):
        for shelf in self.shelves:
            if any(book.book_id == book_id for book in shelf.books):
                return True
        return False