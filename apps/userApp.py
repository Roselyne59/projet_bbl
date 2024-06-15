from managers.userManager import UserManager
import tkinter as tk
from tkinter import ttk
from models.user import User
from tkinter import messagebox
from tkcalendar import DateEntry
import re

class UserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Utilisateurs")
        
        # Get screen dimension
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Main window dimension (percentage of screen size)
        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)

        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        # Window geometry
        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")
                           
        self.user_manager = UserManager()

        #Search user by name button
        self.search_label = tk.Label(self.root, font=('Helvetica', 10, 'bold'), text="Recherche par nom")
        self.search_label.pack(pady=10)
        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack(pady=10)
        self.search_button = tk.Button(self.root, text="Rechercher", font=('Helvetica', 10, 'bold'), command=lambda : self.search_user(self.tree))
        self.search_button.pack(pady=10)

        #Refresh users list button
        self.refresh_list_button = tk.Button(self.root, text="Actualiser la liste", font=('Helvetica', 10, 'bold'), command=lambda : self.refresh_list(self.tree))
        self.refresh_list_button.pack(pady=10)

         # Treeview for displaying users
        self.tree = ttk.Treeview(self.root, columns=('ID', 'Nom', 'Prénom', 'Date de naissance', 'Email', 'Rue et Numéro', 'Code postal', 'Login', 'Password', 'Admin'), show='headings')
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Define headings
        self.tree.heading('ID', text='ID')
        self.tree.heading('Nom', text='Nom')
        self.tree.heading('Prénom', text='Prénom')
        self.tree.heading('Date de naissance', text='Date de naissance')
        self.tree.heading('Email', text='Email')
        self.tree.heading('Rue et Numéro', text='Rue et Numéro')
        self.tree.heading('Code postal', text='Code postal')
        self.tree.heading('Login', text='Login')
        self.tree.heading('Password', text='Password')
        self.tree.heading('Admin', text='Admin')

        # Define column widths
        self.tree.column('ID', width=50)
        self.tree.column('Nom', width=100)
        self.tree.column('Prénom', width=100)
        self.tree.column('Date de naissance', width=100)
        self.tree.column('Email', width=150)
        self.tree.column('Rue et Numéro', width=150)
        self.tree.column('Code postal', width=100)
        self.tree.column('Login', width=100)
        self.tree.column('Password', width=100)
        self.tree.column('Admin', width=50)

        #Column headers style
        #style = ttk.Style()
        #style.configure("Treeview.Heading", font=('Helvetica', 10, 'bold'))

        # Frame for aligning buttons horizontally
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.add_button = tk.Button(button_frame, text="Ajouter Utilisateur", font=('Helvetica', 10, 'bold'), command=self.show_user_form)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.modify_button = tk.Button(button_frame, text="Modifier Utilisateur", font=('Helvetica', 10, 'bold'), command=self.modify_user_form)
        self.modify_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(button_frame, text="Supprimer Utilisateur", font=('Helvetica', 10, 'bold'), command=self.delete_user)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        self.update_treeview()
    
    #Search user by firstname
    def search_user(self, treeview):
        search_term = self.search_entry.get().strip().lower()
        filtered_users = [user for user in self.user_manager.users if search_term in user.firstname.lower()]
        self.show_search_results(treeview, filtered_users)
     
    #Display the search Result in th treeview in parameters
    def show_search_results(self, treeview, filtered_users):
        for item in treeview.get_children():
            treeview.delete(item)
        for user in filtered_users:
            treeview.insert('', 'end', values=(user.user_id, user.firstname, user.lastname, user.birthdate, user.email, user.street, user.zip_code, user.login, user.password, user.is_admin))
    
    #Refresh user list
    def refresh_list(self, treeview):
        self.update_treeview()

    #Update selected user
    def modify_user_form(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Attention", "Veuillez sélectionner un utilisateur à modifier.")
            return
        selected_user_id = self.tree.item(selected_item[0])['values'][0]
        user = next((u for u in self.user_manager.users if u.user_id == selected_user_id), None)
        self.show_user_form(user)
   
    def delete_user(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Attention", "Veuillez sélectionner un utilisateur à supprimer.")
            return
        selected_user_id = self.tree.item(selected_item[0])['values'][0]
        self.user_manager.remove_user(selected_user_id)
        self.update_treeview()

    #Add user or modify existing one
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

        validate_street_cmd = (self.form_window.register(self.validate_street), '%P')

        self.street_label = tk.Label(self.form_window, text="Rue et Numéro: ") 
        self.street_label.grid(row=5, column=0, sticky='E')
        self.street_entry = tk.Entry(self.form_window, validate="key", validatecommand=validate_street_cmd)
        self.street_entry.grid(row=5, column=1)
        self.street_entry.insert(0, user.street if user else "")

        self.zip_code_label = tk.Label(self.form_window, text="Code postal :") 
        self.zip_code_label.grid(row=6, column=0, sticky='E')
        self.zip_code_entry = tk.Entry(self.form_window)
        self.zip_code_entry.grid(row=6, column=1)
        self.zip_code_entry.insert(0, user.zip_code if user else "")

        self.login_label = tk.Label(self.form_window, text="Login:")
        self.login_label.grid(row=7, column=0, sticky='E')
        self.login_entry = tk.Entry(self.form_window)
        self.login_entry.grid(row=7, column=1)
        self.login_entry.insert(0, user.login if user else "")
        #Check login format
        self.login_entry.bind('<FocusOut>', self.check_login)

        self.password_label = tk.Label(self.form_window, text="Password:")
        self.password_label.grid(row=8, column=0, sticky='E')
        self.password_entry = tk.Entry(self.form_window, show="*")
        self.password_entry.grid(row=8, column=1)
        self.password_entry.insert(0, user.password if user else "")
        self.password_entry.bind('<FocusOut>', self.check_password_format)

        self.is_admin_label = tk.Label(self.form_window, text="Admin :")
        self.is_admin_label.grid(row=9, column=0, sticky='E')
        self.is_admin_var = tk.BooleanVar()
        self.is_admin_var.set(user.is_admin if user else False)
        self.is_admin_checkbutton = tk.Checkbutton(self.form_window, text="Oui", variable=self.is_admin_var)
        self.is_admin_checkbutton.grid(row=9, column=1)

        self.submit_button = tk.Button(self.form_window, text="Valider", font=('Helvetica', 10, 'bold'), command=lambda: self.save_user(user))
        self.submit_button.grid(row=10, column=0, columnspan=2)
    
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
    
    #Street and number entry validation (allow only alphabetic, "-" and " " and digits)
    def validate_street(self, value_if_allowed):
        if re.match("^[A-Za-zÀ-ÿ0-9 -]*$", value_if_allowed):
            return True
        else:
            return False

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
        street = self.street_entry.get()
        zip_code = self.zip_code_entry.get()
        login = self.login_entry.get()
        password = self.password_entry.get()
        is_admin = self.is_admin_var.get()

        if not all([first_name, last_name, birthdate, email, street , zip_code, login, password]):
            messagebox.showwarning("Attention", "Tous les champs doivent être remplis.")
            return

        new_user = User(user_id, first_name, last_name, birthdate, email, street, zip_code, login, password, is_admin)

        if old_user:
            self.user_manager.update_user(new_user)
        else:
            self.user_manager.add_user(new_user)

        self.update_treeview()
        self.form_window.destroy()

    def update_treeview(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        for user in self.user_manager.users:
            self.tree.insert('', 'end', values=(user.user_id, 
                                                user.firstname, 
                                                user.lastname, 
                                                user.birthdate, 
                                                user.email, 
                                                user.street, 
                                                user.zip_code, 
                                                user.login, 
                                                user.password, 
                                                user.is_admin))
