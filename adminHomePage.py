import tkinter as tk
from memberHomePage import MemberHomePage
from userApp import UserApp
from book

class AdminHomePage(MemberHomePage):
    def __init__(self, root):
        super().__init__(root)
        self.root.title("Espace Administrateur")

        self.admin_page_title()

    def admin_page_title(self):
        title_label = tk.Label(self.root, text="Bibliothèque", font =('Helvetica', 24, "Bold"))
        title_label.pack (pady=20)

    def admin_page_buttons(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand = True)

        Self.user_button = tk.Button(button_frame, text="Utilisateurs", command=)

        