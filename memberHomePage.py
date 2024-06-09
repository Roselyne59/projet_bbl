import tkinter as tk

class MemberHomePage:
    def __init__(self, root, nom, prenom):
        self.root = root
        self.clear_screen()
        self.root.title("Espace Membre")

        self.welcome_message(nom, prenom)

        
    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def welcome_message(self, nom, prenom):
        welcome_message= f"Bienvenue {nom} {prenom}"
        welcome_label = tk.Label(self.root, text = welcome_message, font=('helvetica', 16, 'bold'), fg='red')
        welcome_label.pack(pady=20)
