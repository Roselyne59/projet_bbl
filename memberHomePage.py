from tkinter import Toplevel
from userHomePage import UserHomePage
from bookApp import BookApp
from reservationApp import ReservationApp
import tkinter as tk

class MemberHomePage(UserHomePage):
    def __init__(self, root, firstname, lastname, user_id):
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
        self.book_app.update_treeview
    
    def open_reservation_app(self):
        reservation_window = Toplevel(self.root)
        app = ReservationApp(reservation_window, self.user_id)
