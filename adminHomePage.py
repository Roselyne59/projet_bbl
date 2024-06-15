import tkinter as tk
from userHomePage import UserHomePage
from userApp import UserApp
from bookApp import BookApp
from shelfApp import ShelfApp
from borrowApp import BorrowApp
from viewAllReservationsApp import ViewAllReservationsApp

class AdminHomePage(UserHomePage):
    def __init__(self, root, firstname, lastname):
        super().__init__(root, firstname, lastname)
        self.root.title("Espace Administrateur")

        self.admin_page_title()
        self.admin_page_buttons()

    def admin_page_title(self):
        title_label = tk.Label(self.root, text="Bibliothèque", font=("Helvetica", 26))
        title_label.pack(pady=20)

    def admin_page_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True)

        self.user_button = tk.Button(button_frame, text="Utilisateurs", width=20, height=2, font=('Helvetica', 10, 'bold'), command=self.open_user_app)
        self.user_button.grid(row=0, column=0, padx=20, pady=20)

        self.book_button = tk.Button(button_frame, text="Livres", width=20, height=2, font=('Helvetica', 10, 'bold'), command=self.open_book_app)
        self.book_button.grid(row=0, column=1, padx=20, pady=20)

        self.shelf_button = tk.Button(button_frame, text="Etagères", width=20, height=2, font=('Helvetica', 10, 'bold'), command=self.open_shelf_app)
        self.shelf_button.grid(row=0, column=2, padx=20, pady=20)

        self.reservation_button = tk.Button(button_frame, text="Résérvations", width=20, height=2, font=('Helvetica', 10, 'bold'), command=self.open_reservation_app)
        self.reservation_button.grid(row=0, column=3, padx=20, pady=20)

        self.borrow_button = tk.Button(button_frame, text="Emprunts", width=20, height=2, font=('Helvetica', 10, 'bold'), command=self.open_borrow_app)
        self.borrow_button.grid(row=0, column=4, padx=20, pady=20)

    def open_user_app(self):
        user_window = tk.Tk()
        UserApp(user_window)

    def open_book_app(self):
        book_window = tk.Tk()
        BookApp(book_window)

    def open_shelf_app(self):
        shelf_window = tk.Tk()
        ShelfApp(shelf_window)

    def open_borrow_app(self):
        borrow_window = tk.Tk()
        BorrowApp(borrow_window)

    def open_reservation_app(self):
        reservation_window = tk.Tk()
        ViewAllReservationsApp(reservation_window)


