"""Create an interface for register"""
from pathlib import Path
import json
import os
import tkinter as tk
from tkinter import ttk


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.frame = ttk.Frame(self.root)
        self.frame = ttk.Frame(self.root, padding="450 250 450 450")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Initialiser les variables pour chaque champ
        labels = ["First Name:", "Last Name:", "Birthdate:", "Email:", "Address:", "Login:", "Password:"]
        self.variables = [tk.StringVar() for _ in labels]

        # Créer les widgets pour chaque champ
        for i, (label, var) in enumerate(zip(labels, self.variables)):
            ttk.Label(self.frame, text=label).grid(column=0, row=i, sticky=tk.W)
            ttk.Entry(self.frame, width=25, textvariable=var).grid(column=1, row=i, sticky=(tk.W, tk.E))

        # Bouton pour s'enregistrer
        ttk.Button(self.frame, text="Register", command=self.register_new_user).grid(column=1, row=len(labels),
                                                                                     sticky=tk.E)

        # Ajouter un peu d'espacement entre les widgets
        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def register_new_user(self):
        # Affichage des informations collectées pour exemple
        user_info = ["First Name", "Last Name", "Birthdate", "Email", "Address", "Login", "Password"]
        for info, var in zip(user_info, self.variables):
            print(f"{info}: {var.get()}")

        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.destroy()
        Login(self.root)


class Login:

    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.initialize_login_widgets()

    def initialize_login_widgets(self):
        self.frame = ttk.Frame(self.root, padding="450 250 450 450")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.login = tk.StringVar()
        self.password = tk.StringVar()

        # Widgets pour la connexion
        ttk.Label(self.frame, text="Login:").grid(column=0, row=0, sticky=tk.W)
        ttk.Entry(self.frame, width=25, textvariable=self.login).grid(column=1, row=0, sticky=(tk.W, tk.E))
        ttk.Label(self.frame, text="Password:").grid(column=0, row=1, sticky=tk.W)
        ttk.Entry(self.frame, width=25, textvariable=self.password).grid(column=1, row=1, sticky=(tk.W, tk.E))
        ttk.Button(self.frame, text="Sign in", command=self.submit).grid(column=2, row=2, sticky=(tk.W, tk.E))
        ttk.Button(self.frame, text="Register a new user", command=self.load_register_form).grid(column=1, row=2,
                                                                                                 sticky=(tk.W, tk.E))
        ttk.Button(self.frame, text="Register a new admin", command=self.load_register_form).grid(column=0, row=2,
                                                                                                  sticky=(tk.W, tk.E))

        # Espacement
        for child in self.frame.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def submit(self):
        print(f"Login: {self.login.get()}")
        print(f"Password: {self.password.get()}")

    def load_register_form(self):
        # Effacer les widgets actuels
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.destroy()

        # Créer une instance de Register
        Register(self.root)


if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
