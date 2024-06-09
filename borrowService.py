# borrow_service.py

import json
import os
from datetime import datetime
from borrow import Borrow

class BorrowService:
    def __init__(self, json_file="json/borrows.json"):
        """
        Initialise le service des emprunts en chargeant les emprunts existants
        depuis le fichier JSON spécifié.
        """
        self.json_file = json_file
        self.borrows = self.load_borrows()

    def load_borrows(self):
        """
        Charge les emprunts depuis un fichier JSON.
        Retourne une liste vide si le fichier n'existe pas.
        """
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r') as file:
            borrows_data = json.load(file)
            return [Borrow(**data) for data in borrows_data]

    def save_borrows(self):
        """
        Sauvegarde la liste des emprunts dans un fichier JSON.
        """
        borrows_data = [vars(borrow) for borrow in self.borrows]
        with open(self.json_file, 'w') as file:
            json.dump(borrows_data, file, indent=4)

    def add_borrow(self, book_id, user_login):
        """
        Ajoute un nouvel emprunt pour un livre et un utilisateur spécifiés.
        """
        new_borrow = Borrow(book_id=book_id, user_login=user_login)
        self.borrows.append(new_borrow)
        self.save_borrows()

    def return_book(self, book_id, user_login):
        """
        Enregistre le retour d'un livre emprunté.
        Met à jour la date de retour de l'emprunt correspondant.
        """
        for borrow in self.borrows:
            if borrow.book_id == book_id and borrow.user_login == user_login and borrow.return_date is None:
                borrow.return_date = datetime.now()
                self.save_borrows()
                return True
        return False

    def delete_borrow(self, book_id, user_login):
        """
        Supprime un emprunt de la liste basé sur l'ID du livre et le login de l'utilisateur.
        """
        self.borrows = [borrow for borrow in self.borrows if not (borrow.book_id == book_id and borrow.user_login == user_login)]
        self.save_borrows()

    def list_borrows(self):
        """
        Retourne la liste de tous les emprunts.
        """
        return self.borrows

    def find_borrow_by_user(self, user_login):
        """
        Trouve tous les emprunts pour un utilisateur donné.
        """
        return [borrow for borrow in self.borrows if borrow.user_login == user_login]

    def find_borrow_by_book(self, book_id):
        """
        Trouve tous les emprunts pour un livre donné.
        """
        return [borrow for borrow in self.borrows if borrow.book_id == book_id]
