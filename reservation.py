from user import User  # Import de la classe User
from book import Book  # Import de la classe Book
import datetime  # Import du module datetime pour la gestion des dates

class Reservation:
    def __init__(self, user, book, reservation_date=None):
        """
        Initialise une réservation avec un utilisateur, un livre et une date de réservation (optionnelle).

        Args:
            user (User): L'utilisateur effectuant la réservation.
            book (Book): Le livre réservé.
            reservation_date (datetime.date, optionnel): La date de la réservation. Si non spécifié, la date actuelle est utilisée.
        """
        self.user = user
        self.book = book
        self.reservation_date = reservation_date or datetime.date.today()
        self.cancelled = False  # Indique si la réservation a été annulée

    def cancel(self):
        """
        Annule la réservation du livre.
        """
        if not self.cancelled:
            self.cancelled = True
            print(f"La réservation du livre '{self.book.title}' par l'utilisateur '{self.user.firstname} {self.user.lastname}' a été annulée.")
        else:
            print("La réservation a déjà été annulée.")

    def update_reservation_date(self, new_date):
        """
        Met à jour la date de réservation.

        Args:
            new_date (datetime.date): La nouvelle date de réservation.
        """
        self.reservation_date = new_date
        print(f"La date de réservation du livre '{self.book.title}' par l'utilisateur '{self.user.firstname} {self.user.lastname}' a été mise à jour.")

    def delete(self):
        """
        Supprime la réservation.
        """
        print(f"La réservation du livre '{self.book.title}' par l'utilisateur '{self.user.firstname} {self.user.lastname}' a été supprimée.")
        del self

