import tkinter as tk
from memberHomePage import MemberHomePage
from userApp import UserApp
from bookApp import BookApp
from shelfApp import ShelfApp


class AdminHomePage(MemberHomePage):
    def __init__(self, root, nom, prenom):
        super().__init__(root, nom, prenom)
        self.root.title("Espace Administrateur")

        self.admin_page_title()
        self.admin_page_buttons()

    def admin_page_title(self):
        title_label = tk.Label(self.root, text="Bibliothèque", font=("Helvetica", 26))
        title_label.pack(pady=20)

    def admin_page_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand= True)

        self.user_button = tk.Button(button_frame, text="Utilisateurs", width=20, height=2, font=('Helvetica', 10, 'bold'), command= self.open_user_app)
        self.user_button.grid(row=0, column=0, padx=20, pady=20)

        self.user_button = tk.Button(button_frame, text="Livres", width=20, height=2, font=('Helvetica', 10, 'bold'), command= self.open_book_app)
        self.user_button.grid(row=0, column=1, padx=20, pady=20)

        self.user_button = tk.Button(button_frame, text="Etagères", width=20, height=2, font=('Helvetica', 10, 'bold'), command= self.open_shelf_app)
        self.user_button.grid(row=0, column=2, padx=20, pady=20)

        self.user_button = tk.Button(button_frame, text="Reservation", width=20, height=2, font=('Helvetica', 10, 'bold'), command= self.open_user_app)
        self.user_button.grid(row=0, column=3, padx=20, pady=20)

        self.user_button = tk.Button(button_frame, text="Emprunts", width=20, height=2, font=('Helvetica', 10, 'bold'), command= self.open_user_app)
        self.user_button.grid(row=0, column=4, padx=20, pady=20)

    def open_user_app(self):
        user_window= tk.Tk()
        UserApp(user_window)
    
    def open_book_app(self):
        user_window= tk.Tk()
        BookApp(user_window)

    def open_shelf_app(self):
        user_window= tk.Tk()
        ShelfApp(user_window)
        
       

        