import tkinter as tk
from tkinter import messagebox
from managers.userManager import UserManager
from homepages.memberHomePage import MemberHomePage
from homepages.adminHomePage import AdminHomePage


class LoginApp:
    """
    GUI Application for user login.

    Attributes:
        root (tk.Tk): The root window of the Tkinter application.
        user_manager (UserManager): Manager for handling users.
        user_app (tk.Frame or None): The user-specific homepage application.
    """
    def __init__(self, root):
        """
        Initializes the LoginApp with the given root window.

        Args:
            root (tk.Tk): The root window of the Tkinter application.
        """
        self.root = root
        self.root.title("Connexion")

        self.user_manager = UserManager()

        self.user_app = None
        
        self.login_page()
    
    def login_page(self):
        """
        Displays the login page.
        """
        self.clear_screen()

        login_frame = tk.Frame(self.root)
        login_frame.grid(row=0, column=0, sticky="nsew")


        for i in range(3):
            login_frame.rowconfigure(i, weight=1)
        login_frame.columnconfigure(0, weight=1)
        login_frame.columnconfigure(1, weight=1)

        self.login_label = tk.Label(login_frame, text="Login")
        self.login_label.grid(row=0, column=0, padx=20, pady=10, sticky="e")
        self.login_entry = tk.Entry(login_frame)
        self.login_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")

        self.password_label = tk.Label(login_frame, text="Mot de passe")
        self.password_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.password_entry = tk.Entry(login_frame, show="*")
        self.password_entry.grid(row=1, column=1, padx=20, pady=10, sticky="w")

        self.login_button = tk.Button(login_frame, text="Se connecter", command=self.check_login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=20)

    def check_login(self):
        """
        Checks the login credentials and opens the appropriate user homepage.

        Displays an error message if the login credentials are incorrect.
        """
        login = self.login_entry.get()
        password = self.password_entry.get()

        user = self.user_manager.get_user_by_login(login)

        if user and user.password == password:
            if user.is_admin:
                self.user_app = AdminHomePage(self.root, user.lastname, user.firstname)
            else:
                self.user_app = MemberHomePage(self.root, user.lastname, user.firstname, user.user_id)
            return

        messagebox.showerror("Erreur", "Login ou mot de passe incorrect.")

    def clear_screen(self):
        """
        Clears the current screen by destroying all widgets in the root window.
        """
        for widget in self.root.winfo_children():
            widget.destroy()

