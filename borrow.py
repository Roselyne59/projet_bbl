# borrow.py

from datetime import datetime

class Borrow:
    def __init__(self, book_id, user_login, borrow_date=None, return_date=None):
        """
        Initialise un emprunt avec l'ID du livre, le login de l'utilisateur,
        la date d'emprunt, et éventuellement la date de retour.
        """
        self.book_id = book_id
        self.user_login = user_login
        self.borrow_date = borrow_date if borrow_date else datetime.now()
        self.return_date = return_date

    def __str__(self):
        """
        Fournit une représentation détaillée de l'objet Borrow,
        utile pour le débogage et l'inspection.
        """
        return (f"Borrow(book_id={self.book_id}, user_login={self.user_login}, "
                f"borrow_date={self.borrow_date}, return_date={self.return_date})")


