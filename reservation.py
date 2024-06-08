# reservation.py

from datetime import datetime

class Reservation:
    def __init__(self, book_id, user_login, reservation_date=None):
        """
        Initialise une réservation de livre.
        
        :param book_id: Identifiant du livre réservé.
        :param user_login: Login de l'utilisateur qui a réservé le livre.
        :param reservation_date: Date de la réservation (par défaut à la date actuelle).
        """
        self.book_id = book_id
        self.user_login = user_login
        self.reservation_date = reservation_date if reservation_date else datetime.now()

    def __repr__(self):
        return (f"Reservation(book_id={self.book_id}, user_login={self.user_login}, "
                f"reservation_date={self.reservation_date})")
