import json
import os
from models.shelf import Shelf

class ShelfManager:
    """_summary_
    """
    def __init__(self, json_file="json/shelves.json"):
        """_summary_

        Args:
            json_file (str, optional): _description_. Defaults to "json/shelves.json".
        """
        self.json_file = json_file
        self.shelves = self.load_shelves()

    def load_shelves(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r', encoding='utf-8') as file:
            shelves_data = json.load(file)
            return [Shelf.from_dict(data) for data in shelves_data]

    def save_shelves(self):
        """_summary_
        """
        with open(self.json_file, 'w', encoding='utf-8') as file:
            json.dump([shelf.to_dict() for shelf in self.shelves], file, ensure_ascii=False, indent=4)
        
    def add_shelf(self, shelf):
        """_summary_

        Args:
            shelf (_type_): _description_

        Raises:
            ValueError: _description_
        """
        if self.is_duplicate(shelf.number, shelf.letter):
            raise ValueError("Une étagère avec cette combinaison existe déjà !")
        self.shelves.append(shelf)
        self.save_shelves()

    def update_shelf(self, old_number, new_shelf):
        """_summary_

        Args:
            old_number (_type_): _description_
            new_shelf (_type_): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
        """
        for i, s in enumerate(self.shelves):
            if s.number == old_number:
                if (new_shelf.number != old_number or new_shelf.letter != s.letter) and self.is_duplicate(new_shelf.number, new_shelf.letter):
                    raise ValueError("Une étagère avec cette combinaison existe déjà !")
                self.shelves[i] = new_shelf
                self.save_shelves()
                return
        raise ValueError("Etagère introuvable...")

    def remove_shelf(self, shelf_id):
        """_summary_

        Args:
            shelf_id (_type_): _description_
        """
        self.shelves = [shelf for shelf in self.shelves if shelf.shelf_id != shelf_id]
        self.update_shelf_ids()
        self.save_shelves()
        
    def update_shelf_ids(self):
        """_summary_
        """
        for i, shelf in enumerate(self.shelves):
            shelf.shelf_id = i + 1
        Shelf.shelf_number = len(self.shelves) + 1

    def add_book_to_shelf(self, shelf_number, book):
        """_summary_

        Args:
            shelf_number (_type_): _description_
            book (_type_): _description_

        Raises:
            ValueError: _description_
            ValueError: _description_
        """
        if self.is_book_in_any_shelf(book.book_id):
            raise ValueError("Ce livre est déjà dans une autre étagère.")
        for shelf in self.shelves:
            if shelf.number == shelf_number:
                shelf.books.append(book)
                self.save_shelves()
                return
        raise ValueError("Etagère introuvable...")

    def remove_book_from_shelf(self, shelf_number, book_id):
        """_summary_

        Args:
            shelf_number (_type_): _description_
            book_id (_type_): _description_

        Raises:
            ValueError: _description_
        """
        for shelf in self.shelves:
            if shelf.number == shelf_number:
                shelf.books = [book for book in shelf.books if book.book_id != book_id]
                self.save_shelves()
                return
        raise ValueError("Etagère introuvable...")
    
    def is_duplicate(self, number, letter):
        """_summary_

        Args:
            number (_type_): _description_
            letter (_type_): _description_

        Returns:
            _type_: _description_
        """
        return any(shelf.number == number and shelf.letter == letter for shelf in self.shelves)
    
    def is_book_in_any_shelf(self, book_id):
        """_summary_

        Args:
            book_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        for shelf in self.shelves:
            if any(book.book_id == book_id for book in shelf.books):
                return True
        return False