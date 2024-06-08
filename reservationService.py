# reservation_service.py
import json
import os
from reservation import Reservation
from book_service import BookService
from user_service import UserService

class ReservationService:
    def __init__(self, json_file="json/reservations.json"):
        """
        Initialise le service de gestion des réservations.
        
        :param json_file: Chemin vers le fichier JSON pour stocker les réservations.
        """
        self.json_file = json_file
        self.reservations = self.load_reservations()
        self.book_service = BookService()
        self.user_service = UserService()

    def load_reservations(self):
        """
        Charge les réservations à partir du fichier JSON.
        
        :return: Liste d'objets Reservation.
        """
        if not os.path.exists(self.json_file):
            return []
        try:
            with open(self.json_file, 'r') as file:
                reservations_data = json.load(file)
                return [Reservation(**data) for data in reservations_data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading reservations: {e}")
            return []

    def save_reservations(self):
        """
        Sauvegarde la liste actuelle des réservations dans le fichier JSON.
        """
        try:
            with open(self.json_file, 'w') as file:
                json.dump([reservation.__dict__ for reservation in self.reservations], file, indent=4)
        except IOError as e:
            print(f"Error saving reservations: {e}")

    def reserve_book(self, book_id, user_login):
        """
        Réserve un livre pour un utilisateur.
        
        :param book_id: Identifiant du livre à réserver.
        :param user_login: Login de l'utilisateur qui réserve le livre.
        :return: True si la réservation a réussi, False sinon.
        """
        book = self.book_service.find_book_by_id(book_id)
        user = self.user_service.validate_credentials(user_login, user_login)  # Simplified validation
        if book and user and not book.reserved_by:
            # Créer une nouvelle réservation
            reservation = Reservation(book_id=book_id, user_login=user_login)
            self.reservations.append(reservation)
            # Met à jour le livre pour indiquer qu'il est réservé
            book.reserved_by = user_login  
            # Sauvegarde l'état des livres
            self.book_service.save_books()  
            # Sauvegarde les réservations
            self.save_reservations()  
            return True
        return False

    def release_book(self, book_id):
        """
        Libère un livre réservé.
        
        :param book_id: Identifiant du livre à libérer.
        :return: True si la libération a réussi, False sinon.
        """
        book = self.book_service.find_book_by_id(book_id)
        if book and book.reserved_by:
            # Trouver la réservation correspondante et la supprimer
            self.reservations = [res for res in self.reservations if res.book_id != book_id]
             # Libérer le livre
            book.reserved_by = None 
            # Sauvegarde l'état des livres
            self.book_service.save_books()  
            # Sauvegarde les réservations
            self.save_reservations()  
            return True
        return False

    def get_reservations(self):
        """
        Retourne la liste actuelle des réservations.
        
        :return: Liste d'objets Reservation.
        """
        return self.reservations



        