import tkinter as tk
from tkinter import ttk, messagebox

from library import Library
from user import User
from userService import UserService
from bookService import BookService

class Register:
    def __init__(self, root, userService, bookService, is_admin=False):
        self.root = root
        self.userService = userService
        self.bookService = bookService
        self.is_admin = is_admin
        self.root.title("Register as Admin" if is_admin else "Register as User")
        self.frame = ttk.Frame(self.root, padding="450 450 450 450")
        self.frame.pack(fill=tk.BOTH, expand=True)

        labels = ["First Name:", "Last Name:", "Birthdate:", "Email:", "Address:", "Login:", "Password:"]
        self.entries = {}
        for i, label in enumerate(labels):
            ttk.Label(self.frame, text=label).grid(row=i, column=0, sticky=tk.W)
            entry = ttk.Entry(self.frame, width=25, show="*" if label == "Password:" else "")
            entry.grid(row=i, column=1, sticky=(tk.W, tk.E))
            self.entries[label] = entry

        ttk.Button(self.frame, text="Register", command=self.register_new_user).grid(row=len(labels), column=1, sticky=tk.E)

    def register_new_user(self):
        user = User(
            firstname=self.entries["First Name:"].get(),
            lastname=self.entries["Last Name:"].get(),
            birthdate=self.entries["Birthdate:"].get(),
            email=self.entries["Email:"].get(),
            address=self.entries["Address:"].get(),
            login=self.entries["Login:"].get(),
            password=self.entries["Password:"].get(),
            is_admin=self.is_admin
        )
        self.userService.add_user(user)
        self.frame.destroy()
        Login(self.root, self.userService, self.bookService)


class Login:
    def __init__(self, root, userService, bookService):
        self.root = root
        self.userService = userService
        self.bookService = bookService
        self.root.title("Login")
        self.setup_widgets()

    def setup_widgets(self):
        self.frame = ttk.Frame(self.root, padding="450 450 450 450")
        self.frame.pack(fill=tk.BOTH, expand=True)

        ttk.Label(self.frame, text="Login:").grid(row=0, column=0, sticky=tk.W)
        self.login = ttk.Entry(self.frame, width=25)
        self.login.grid(row=0, column=1, sticky=(tk.W, tk.E))

        ttk.Label(self.frame, text="Password:").grid(row=1, column=0, sticky=tk.W)
        self.password = ttk.Entry(self.frame, width=25, show="*")
        self.password.grid(row=1, column=1, sticky=(tk.W, tk.E))

        ttk.Button(self.frame, text="Connexion", command=self.submit).grid(row=2, column=2, sticky=tk.E)
        ttk.Button(self.frame, text="Inscrire utilisateur", command=lambda: self.load_register_form(False)).grid(row=2, column=0, sticky=tk.W)
        ttk.Button(self.frame, text="Inscrire administrateur", command=lambda: self.load_register_form(True)).grid(row=2, column=1, sticky=tk.E + tk.W)

    def submit(self):
        username = self.login.get()
        password = self.password.get()
        user = self.userService.validate_credentials(username, password)
        if user:
            self.launch_library(user)
        else:
            messagebox.showerror("Login Failed", "The username or password is incorrect")

    def launch_library(self, user):
        self.frame.destroy()
        Library(self.root, self.bookService, self.userService, user)

    def load_register_form(self, is_admin):
        self.frame.destroy()
        Register(self.root, self.userService, self.bookService, is_admin)
