from user import User  # Import de la classe User
from book import Book  # Import de la classe Book
import datetime  # Import du module datetime pour la gestion des dates

class Borrow:
    def __init__(self, user, book, borrow_date=None):
        """
        Initialise un emprunt avec un utilisateur, un livre et une date d'emprunt (optionnelle).

        Args:
            user (User): L'utilisateur qui emprunte le livre.
            book (Book): Le livre emprunté.
            borrow_date (datetime.date, optionnel): La date d'emprunt. Si non spécifiée, la date actuelle est utilisée.
        """
        self.user = user
        self.book = book
        self.borrow_date = borrow_date or datetime.date.today()
        self.returned = False  # Indique si le livre a été retourné

    def return_book(self):
        """
        Marque le livre comme retourné.
        """
        if not self.returned:
            self.returned = True
            print(f"Le livre '{self.book.title}' a été retourné par l'utilisateur '{self.user.firstname} {self.user.lastname}'.")
        else:
            print("Le livre a déjà été retourné.")
