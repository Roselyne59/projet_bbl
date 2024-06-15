from tkinter import Toplevel
from homepages.userHomePage import UserHomePage
from apps.bookApp import BookApp
from apps.reservationApp import ReservationApp
import tkinter as tk

class MemberHomePage(UserHomePage):
    """
    GUI Application for the member home page.

    Inherits from UserHomePage and adds member-specific functionalities.

    Attributes:
        root (tk.Tk): The root window of the Tkinter application.
        firstname (str): The first name of the member.
        lastname (str): The last name of the member.
        user_id (int): The ID of the member.
        book_app (BookApp): An instance of the BookApp for displaying books.
        reservation_button (tk.Button): A button to open the reservation app.
    """
    def __init__(self, root, firstname, lastname, user_id):
        """
        Initializes the MemberHomePage with the given root window, first name, last name, and user ID.

        Args:
            root (tk.Tk): The root window of the Tkinter application.
            firstname (str): The first name of the member.
            lastname (str): The last name of the member.
            user_id (int): The ID of the member.
        """
        super().__init__(root, firstname, lastname)
        self.root = root
        self.user_id = user_id
        self.clear_screen()
        self.root.title("Espace Membre")

        self.welcome_message(firstname, lastname)
        self.logout_bouton()

        self.book_app = BookApp(root, show_books_buttons=False)
        self.show_book_list()

        self.reservation_button = tk.Button(root, text="Faire une réservation", command=self.open_reservation_app)
        self.reservation_button.pack(pady=10)

    def show_book_list(self):
        """
                Displays the list of books.
        """
        self.book_app.update_treeview
    
    def open_reservation_app(self):
        """
        Opens the ReservationApp in a new window.
        """
        reservation_window = Toplevel(self.root)
        app = ReservationApp(reservation_window, self.user_id)
