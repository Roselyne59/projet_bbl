import json
import os
from datetime import datetime


class Borrow:
    def __init__(self, book_id, user_login, borrow_date=None, return_date=None):
        self.book_id = book_id
        self.user_login = user_login
        self.borrow_date = borrow_date if borrow_date else datetime.now()
        self.return_date = return_date

    def __repr__(self):
        return (f"Borrow(book_id={self.book_id}, user_login={self.user_login}, "
                f"borrow_date={self.borrow_date}, return_date={self.return_date})")


class BorrowService:
    def __init__(self, json_file="json/borrows.json"):
        self.json_file = json_file
        self.borrows = self.load_borrows()

    def load_borrows(self):
        """Charge les emprunts à partir du fichier JSON"""
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r') as file:
            borrows_data = json.load(file)
            return [Borrow(**data) for data in borrows_data]

    def save_borrows(self):
        """Sauvegarde les emprunts dans le fichier JSON"""
        borrows_data = [vars(borrow) for borrow in self.borrows]
        with open(self.json_file, 'w') as file:
            json.dump(borrows_data, file, indent=4)

    def add_borrow(self, book_id, user_login):
        """Ajoute un nouvel emprunt"""
        new_borrow = Borrow(book_id=book_id, user_login=user_login)
        self.borrows.append(new_borrow)
        self.save_borrows()

    def return_book(self, book_id, user_login):
        """Enregistre le retour d'un livre emprunté"""
        for borrow in self.borrows:
            if borrow.book_id == book_id and borrow.user_login == user_login and borrow.return_date is None:
                borrow.return_date = datetime.now()
                self.save_borrows()
                return True
        return False

    def delete_borrow(self, book_id, user_login):
        """Supprime un emprunt de la liste"""
        self.borrows = [borrow for borrow in self.borrows if not (borrow.book_id == book_id and borrow.user_login == user_login)]
        self.save_borrows()

    def list_borrows(self):
        """Liste tous les emprunts"""
        return self.borrows

    def find_borrow_by_user(self, user_login):
        """Trouve les emprunts d'un utilisateur"""
        return [borrow for borrow in self.borrows if borrow.user_login == user_login]

    def find_borrow_by_book(self, book_id):
        """Trouve les emprunts d'un livre"""
        return [borrow for borrow in self.borrows if borrow.book_id == book_id]
