import tkinter as tk
from tkinter import ttk


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Déclaration des variables pour les entrées
        self.firstname = tk.StringVar()
        self.lastname = tk.StringVar()
        self.birthdate = tk.StringVar()
        self.email = tk.StringVar()
        self.address = tk.StringVar()
        self.login = tk.StringVar()
        self.password = tk.StringVar()

        # Configurer les widgets
        self.setup_widgets()

    def setup_widgets(self):
        # Créer et positionner les widgets
        labels = ["First Name:", "Last Name:", "Birthdate:", "Email:", "Address:", "Login:", "Password:"]
        variables = [self.firstname, self.lastname, self.birthdate, self.email, self.address, self.login, self.password]
        for i, (label, var) in enumerate(zip(labels, variables)):
            ttk.Label(self.frame, text=label).grid(column=0, row=i, sticky=tk.W)
            ttk.Entry(self.frame, width=25, textvariable=var).grid(column=1, row=i, sticky=(tk.W, tk.E))

        # Bouton pour s'enregistrer
        ttk.Button(self.frame, text="Register", command=self.register_new_user).grid(column=1, row=len(labels), sticky=tk.E)

        # Ajouter un peu d'espacement entre les widgets
        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=5)


