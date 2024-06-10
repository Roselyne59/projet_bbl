import tkinter as tk
from bookApp import BookApp

class MemberHomePage:
    def __init__(self, root, nom, prenom):
        self.root = root
        self.clear_screen()
        self.root.title("Espace Membre")

        self.welcome_message(nom, prenom)
        self.logout_bouton()

        self.book_app = BookApp(root)
        self._show_book_list()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def welcome_message(self, nom, prenom):
        welcome_message= f"Bienvenue {nom} {prenom}"
        welcome_label = tk.Label(self.root, text = welcome_message, font=('helvetica', 16, 'bold'), fg='red')
        welcome_label.pack(pady=20)
    
    def logout_bouton(self):
        logout_button = tk.Button(self.root, text = "Se deconnecter", command=self.logout)
        logout_button.pack(pady=20)

    def logout(self):
        self.clear_screen()
        from login import LoginApp #Avoid cicular import between LoginApp and MemberHomePage
        LoginApp(self.root)
    
    def _show_book_list(self):
        self.book_app.update_list()
    

