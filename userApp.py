from userManager import UserManager
import tkinter as tk
from user import User
from tkinter import messagebox
from tkcalendar import DateEntry
import re

class UserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Utilisateurs")
        # Main window dimension
        window_width = 1080
        window_height = 760

        # Get screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        
        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        # Définir la géométrie de la fenêtre
        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
                           
        self.user_manager = UserManager()

        self.listbox = tk.Listbox(self.root, width=150, height=30)
        self.listbox.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Ajouter Utilisateur", command=self.show_user_form)
        self.add_button.pack(pady=10)
        self.modify_button = tk.Button(self.root, text="Modifier Utilisateur", command=self.modify_user_form)
        self.modify_button.pack(pady=10)
        self.delete_button = tk.Button(self.root, text="Supprimer Utilisateur", command=self.delete_user)
        self.delete_button.pack(pady=10)

        self.update_listbox()

    def modify_user_form(self):
        selected_user_index = self.listbox.curselection()
        if not selected_user_index:
            messagebox.showwarning("Attention", "Veuillez sélectionner un utilisateur à modifier.")
            return

        user_id = int(self.listbox.get(selected_user_index[0]).split(":")[1].strip())
        user = next((u for u in self.user_manager.users if u.user_id == user_id), None)

        self.show_user_form(user)

    def delete_user(self):
        selected_user_index = self.listbox.curselection()
        if not selected_user_index:
            messagebox.showwarning("Attention", "Veuillez sélectionner un utilisateur à supprimer.")
            return

        user_id = int(self.listbox.get(selected_user_index[0]).split(":")[1].strip())
        self.user_manager.remove_user(user_id)
        self.update_listbox()

    def show_user_form(self, user=None):
        self.form_window = tk.Toplevel(self.root)
        self.form_window.title("Formulaire Utilisateur")

        window_width = 700
        window_height = 350

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        # User_form window geometry
        self.form_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        user_id = user.user_id if user else User.user_number

        self.user_id_label = tk.Label(self.form_window, text="N°:")
        self.user_id_label.grid(row=0, column=0, sticky='E')
        self.user_id_entry = tk.Entry(self.form_window, state='readonly', textvariable=tk.StringVar(self.form_window, value=str(user_id)))
        self.user_id_entry.grid(row=0, column=1)

        validate_cmd = (self.form_window.register(self.validate_alphabetic), '%P')

        self.first_name_label = tk.Label(self.form_window, text="Nom:")
        self.first_name_label.grid(row=1, column=0, sticky='E')
        self.first_name_entry = tk.Entry(self.form_window, validate="key", validatecommand=validate_cmd)
        self.first_name_entry.grid(row=1, column=1)
        self.first_name_entry.insert(0, user.firstname if user else "")
        self.first_name_entry.focus_set()  # Default cursor on this field

        self.last_name_label = tk.Label(self.form_window, text="Prénom:")
        self.last_name_label.grid(row=2, column=0, sticky='E')
        self.last_name_entry = tk.Entry(self.form_window, validate="key", validatecommand=validate_cmd)
        self.last_name_entry.grid(row=2, column=1)
        self.last_name_entry.insert(0, user.lastname if user else "")

        self.birthdate_label = tk.Label(self.form_window, text="Date de naissance:") 
        self.birthdate_label.grid(row=3, column=0, sticky='E')
        self.birthdate_entry = DateEntry(self.form_window, date_pattern='dd/mm/yyyy', selectmode='day', year=2000, month=1, day=1)
        self.birthdate_entry.grid(row=3, column=1)
        self.birthdate_entry.configure(width=17)
        if user:
            self.birthdate_entry.set_date(user.birthdate)
 
        self.email_label = tk.Label(self.form_window, text="Email:")  
        self.email_label.grid(row=4, column=0, sticky='E')
        self.email_entry = tk.Entry(self.form_window)
        self.email_entry.grid(row=4, column=1)
        self.email_entry.insert(0, user.email if user else "")
        # Check email format
        self.email_entry.bind('<FocusOut>', self.check_email_format)  

        self.address_label = tk.Label(self.form_window, text="Adresse:") 
        self.address_label.grid(row=5, column=0, sticky='E')
        self.address_entry = tk.Entry(self.form_window)
        self.address_entry.grid(row=5, column=1)
        self.address_entry.insert(0, user.address if user else "")

        self.login_label = tk.Label(self.form_window, text="Login:")
        self.login_label.grid(row=6, column=0, sticky='E')
        self.login_entry = tk.Entry(self.form_window)
        self.login_entry.grid(row=6, column=1)
        self.login_entry.insert(0, user.login if user else "")
        #Check login format
        self.login_entry.bind('<FocusOut>', self.check_login)

        self.password_label = tk.Label(self.form_window, text="Password:")
        self.password_label.grid(row=7, column=0, sticky='E')
        self.password_entry = tk.Entry(self.form_window, show="*")
        self.password_entry.grid(row=7, column=1)
        self.password_entry.insert(0, user.password if user else "")
        self.password_entry.bind('<FocusOut>', self.check_password_format)

        self.is_admin_label = tk.Label(self.form_window, text="Admin :")
        self.is_admin_label.grid(row=8, column=0, sticky='E')
        self.is_admin_var = tk.BooleanVar()
        self.is_admin_var.set(user.is_admin if user else False)
        self.is_admin_checkbutton = tk.Checkbutton(self.form_window, text="Oui", variable=self.is_admin_var)
        self.is_admin_checkbutton.grid(row=8, column=1)

        self.submit_button = tk.Button(self.form_window, text="Valider", command=lambda: self.save_user(user))
        self.submit_button.grid(row=9, column=0, columnspan=2)
    
    #Firstname and Lastename entry validation (allow only alphabetic, "-" and " ")
    def validate_alphabetic(self, value_if_allowed):
        if re.match("^[A-Za-zÀ-ÿ -]*$", value_if_allowed):
            return True
        else:
            return False
    #Email entry format validation
    def check_email_format(self, event):
        email = self.email_entry.get()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            messagebox.showerror("Erreur", "Format de l'email invalide. Veuillez entrer un email valide.")
            self.email_entry.focus_set()

    #check if login exists
    def check_login(self, event):
        current_login = self.login_entry.get()
        if self.user_manager.login_exists(current_login):
            messagebox.showerror("Erreur", "Ce login existe déjà. Choisissez un autre.")
            self.login_entry.delete(0, tk.END)
            self.login_entry.focus_set()
            # Mettez à jour l'état du login
            self.valid_login = False
        else:
            # If login valid
            self.valid_login = True

# Check password format
    def check_password_format(self, event):
        # Check login validation before password validation
        if self.valid_login:
            password = self.password_entry.get()
            if not re.match(r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", password):
                messagebox.showerror("Erreur", "Le mot de passe doit comporter au moins 8 caractères, "
                                            "une majuscule, un chiffre et un caractère spécial.")
                self.password_entry.focus_set()
        else:
            pass
    
    #Create new user, or modify existing
    def save_user(self, old_user=None):
        user_id = int(self.user_id_entry.get())
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        birthdate = self.birthdate_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        login = self.login_entry.get()
        password = self.password_entry.get()
        is_admin = self.is_admin_var.get()

        if not all([first_name, last_name, birthdate, email, address, login, password]):
            messagebox.showwarning("Attention", "Tous les champs doivent être remplis.")
            return

        new_user = User(user_id, first_name, last_name, birthdate, email, address, login, password, is_admin)

        if old_user:
            self.user_manager.update_user(new_user)
        else:
            self.user_manager.add_user(new_user)

        self.update_listbox()
        self.form_window.destroy()

    def update_listbox(self):                   #mettre la vielle version pour eviter le bug de la selection du user à modifier ou à supprimer
        self.listbox.delete(0, tk.END)
        for user in self.user_manager.users:
            self.listbox.insert(tk.END, f"Numero : {user.user_id}")
            user_info = [
                f"Nom : {user.firstname}",
                f"Prénom : {user.lastname}",
                f"Date de naissance : {user.birthdate}",
                f"Email : {user.email}",
                f"Adresse : {user.address}",
                f"Login : {user.login}",
                f"Password : {user.password}",
                f"Admin : {user.is_admin}"
            ]
            for item in user_info:
                self.listbox.insert(tk.END, item)
            self.listbox.insert(tk.END, "------------------------------")