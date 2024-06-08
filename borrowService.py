import os
import json
from borrow import Borrow

class BorrowService:
    def __init__(self, json_file="borrows.json"):
        self.json_file = json_file
        self.borrows = self.load_borrows()

    def load_borrows(self):
        """
        Charge les emprunts depuis le fichier JSON.

        Returns:
            list: Une liste d'objets Borrow chargés depuis le fichier JSON.
        """
        if not os.path.exists(self.json_file):
            return []
        try:
            with open(self.json_file, 'r') as file:
                borrows_data = json.load(file)
                return [Borrow(**borrow_data) for borrow_data in borrows_data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Erreur de chargement des emprunts: {e}")
            return []

    def save_borrows(self):
        """
        Sauvegarde les emprunts dans le fichier JSON.
        """
        try:
            with open(self.json_file, 'w') as file:
                json.dump([borrow.__dict__ for borrow in self.borrows], file, indent=4)
        except IOError as e:
            print(f"Erreur de sauvegarde des emprunts: {e}")

    def add_borrow(self, borrow):
        """
        Ajoute un nouvel emprunt.

        Args:
            borrow (Borrow): L'objet Borrow à ajouter.
        """
        self.borrows.append(borrow)
        self.save_borrows()

    def remove_borrow(self, borrow):
        """
        Supprime un emprunt.

        Args:
            borrow (Borrow): L'objet Borrow à supprimer.
        """
        self.borrows.remove(borrow)
        self.save_borrows()
