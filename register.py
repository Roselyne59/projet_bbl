import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import re
import json
import os
from user import User

class Register:
    def __init__(self, root, userService, bookService, is_admin=False):
        self.root = root
        self.userService = userService
        self.bookService = bookService
        self.root.title("Register as Admin" if is_admin else "Register as User")
        self.frame = ttk.Frame(self.root)
        self.frame.place(x=220, y=650)

        self.is_admin_var = tk.BooleanVar(value=is_admin)
        self.create_form()
        self.load_postal_codes()


    def create_form(self):
        labels = ["First Name:", "Last Name:", "Birthdate:", "Email:", "Postal Code:", "Locality:", "Street Address:", "House Number:", "Login:", "Password:"]
        self.entries = {}

        for i, label in enumerate(labels):
            ttk.Label(self.frame, text=label).grid(row=i, column=0, sticky=tk.W)
            if label == "Birthdate:":
                entry = DateEntry(self.frame, width=25, background='darkblue', foreground='white', borderwidth=2,
                                  year=1999, date_pattern='dd/mm/yyyy')
            else:
                entry = ttk.Entry(self.frame, width=25, show="*" if label == "Password:" else "")
            entry.grid(row=i, column=1, sticky=(tk.W, tk.E))
            self.entries[label] = entry

        ttk.Checkbutton(self.frame, text="Is Admin?", variable=self.is_admin_var).grid(row=10, column=1, sticky=tk.W)
        self.entries["Postal Code:"].bind("<KeyRelease>", self.update_locality)
        ttk.Button(self.frame, text="Register", command=self.register_new_user).grid(row=11, column=1, sticky=tk.E)
        ttk.Button(self.frame, text="Cancel", command=self.cancel_registration).grid(row=11, column=0, sticky=tk.W,
                                                                                     pady=10)

    def load_postal_codes(self):
        json_file = os.path.join(os.path.dirname(__file__), 'json', 'code-postaux-belge.json')
        with open(json_file, 'r') as file:
            self.postal_data = json.load(file)

    def update_locality(self, event):
        postal_code = self.entries["Postal Code:"].get()
        localities = [item['column_2'] for item in self.postal_data if item['column_1'] == postal_code]
        if localities:
            locality = localities[0]
        else:
            locality = ""
        self.entries["Locality:"].delete(0, tk.END)
        self.entries["Locality:"].insert(0, locality)

    def validate_email(self, email):
        return re.match(r"[^@]+@[^@]+\.[a-zA-Z]{2,}$", email) is not None

    def validate_password(self, password, login):
        return (password != login and len(password) >= 8 and re.search(r"[A-Z]", password) and re.search(r"\d", password))

    def register_new_user(self):
        errors = []
        for label, entry in self.entries.items():
            if not entry.get():
                errors.append(f"{label} is required")

        email = self.entries["Email:"].get()
        if not self.validate_email(email):
            errors.append("Email format is invalid")

        login = self.entries["Login:"].get()
        if self.userService.is_login_taken(login):
            errors.append("Login is already taken")

        password = self.entries["Password:"].get()
        if not self.validate_password(password, login):
            errors.append(
                "Password must be different from login, contain at least one uppercase letter, one digit, and be at least 8 characters long")

        postal_code = self.entries["Postal Code:"].get()
        locality = self.entries["Locality:"].get()
        if not any(pc['column_1'] == postal_code and pc['column_2'].lower() == locality.lower() for pc in
                   self.postal_data):
            errors.append("Invalid postal code or locality")

        if errors:
            messagebox.showerror("Registration Error", "\n".join(errors))
            return

        address = f"{self.entries['Street Address:'].get()}, {self.entries['House Number:'].get()}, {postal_code} {locality}"

        birthdate = self.entries["Birthdate:"].get_date().strftime('%d/%m/%Y')

        user = User(
            firstname=self.entries["First Name:"].get(),
            lastname=self.entries["Last Name:"].get(),
            birthdate=birthdate,
            email=self.entries["Email:"].get(),
            address=address,
            login=login,
            password=password,
            is_admin=self.is_admin_var.get()
        )
        self.userService.add_user(user)
        self.frame.destroy()

    def cancel_registration(self):
        # Détruire tous les widgets du formulaire
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.frame.destroy()  # Détruire le cadre contenant le formulaire



