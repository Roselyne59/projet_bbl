import tkinter as tk
from tkinter import ttk, messagebox
from userManager import UserManager
import json
#from library import Library


class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Connexion")

        self.user_manager = UserManager()
        
        self.login_page()

    def login_page(self):
        self.clear_screen()

        login_frame = tk.Frame(self.root)
        login_frame.grid(row=0, column=0, sticky="nsew")

        # Configure rows and columns of the frame to be resizable
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
        login = self.login_entry.get()
        password = self.password_entry.get()

        # Load users from JSON
        with open('users.json', 'r') as file:
            users = json.load(file)

        # Check login credentials
        for user in users:
            if user['login'] == login and user['password'] == password:
                if user['is_admin']:
                    self.admin_home_page()
                else:
                    self.member_home_page()
                return
        
        messagebox.showerror("Erreur", "Login ou mot de passe incorrect.")

    def admin_home_page(self):
        self.clear_screen()
        self.root.title("Interface Admin")

        # Add the rest of your admin interface code here
        # For example, you can call self.main_interface() if it is the same as admin interface

    def member_home_page(self):
        self.clear_screen()
        self.root.title("Interface Utilisateur")

        # Add the rest of your user interface code here
        # For example, you can call self.main_interface() if it is the same as user interface

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    

#if __name__ == "__main__":
 #   root = tk.Tk()
  #  app = LoginApp(root)
   #"" root.mainloop()

