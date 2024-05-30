"""Create an interface for register"""
from pathlib import Path
import json
import os
import tkinter as tk
from tkinter import ttk
from register import Register


class Login:

    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.initialize_login_widgets()

    def initialize_login_widgets(self):
        self.frame = ttk.Frame(self.root, padding="450 450 450 450")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.login = tk.StringVar()
        self.password = tk.StringVar()

        # Widgets pour la connexion
        ttk.Label(self.frame, text="Login:").grid(column=0, row=0, sticky=tk.W)
        ttk.Entry(self.frame, width=25, textvariable=self.login).grid(column=1, row=0, sticky=(tk.W, tk.E))
        ttk.Label(self.frame, text="Password:").grid(column=0, row=1, sticky=tk.W)
        ttk.Entry(self.frame, width=25, textvariable=self.password).grid(column=1, row=1, sticky=(tk.W, tk.E))
        ttk.Button(self.frame, text="Sign in", command=self.submit).grid(column=1, row=2, sticky=tk.E)
        ttk.Button(self.frame, text="Register", command=self.load_register_form).grid(column=0, row=2, sticky=tk.W)

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

        # Réinitialiser le titre de la fenêtre
        self.root.title("Register")

        # Widgets pour l'enregistrement
        labels = ["First Name:", "Last Name:", "Birthdate:", "Email:", "Address:", "Login:", "Password:"]
        variables = [tk.StringVar() for _ in labels]  # Crée une nouvelle variable pour chaque champ

        for i, (label, var) in enumerate(zip(labels, variables)):
            ttk.Label(self.frame, text=label).grid(column=0, row=i, sticky=tk.W)
            ttk.Entry(self.frame, width=25, textvariable=var).grid(column=1, row=i, sticky=(tk.W, tk.E))

        # Bouton pour s'enregistrer
        ttk.Button(self.frame, text="Register", command=lambda: self.register_new_user(variables)).grid(column=1, row=len(labels), sticky=tk.E)

    def register_new_user(self, variables):
        # Affichage des informations collectées pour exemple
        user_info = ["First Name", "Last Name", "Birthdate", "Email", "Address", "Login", "Password"]
        for info, var in zip(user_info, variables):
            print(f"{info}: {var.get()}")

        # Effacer les champs après l'enregistrement
        for var in variables:
            var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = Login(root)
    root.mainloop()
