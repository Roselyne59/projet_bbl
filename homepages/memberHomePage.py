from tkinter import Toplevel
from homepages.userHomePage import UserHomePage
from apps.bookApp import BookApp
from apps.reservationApp import ReservationApp
import tkinter as tk

class MemberHomePage(UserHomePage):
    """_summary_

    Args:
        UserHomePage (_type_): _description_
    """
    def __init__(self, root, firstname, lastname, user_id):
        """_summary_

        Args:
            root (_type_): _description_
            firstname (_type_): _description_
            lastname (_type_): _description_
            user_id (_type_): _description_
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
        """_summary_
        """
        self.book_app.update_treeview
    
    def open_reservation_app(self):
        """_summary_
        """
        reservation_window = Toplevel(self.root)
        app = ReservationApp(reservation_window, self.user_id)
