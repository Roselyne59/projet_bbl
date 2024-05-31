import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

class User:
    user_number = 0
    def __init__(self, user_id, firstname, lastname, birthdate, email, address, is_admin=False):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.email = email
        self.address = address
        self.user_id = User.user_number
        User.user_number+=1
        self.is_admin = is_admin
    
    def to_dict(self):              #ajouter le user_Id
        return {
            "user_id": self.user_id,
            "nom": self.firstname,  
            "prenom": self.lastname,
            "date_de_naissance": self.birthdate,  
            "email": self.email,
            "adresse": self.address,
            "is_admin": self.is_admin
        }

    @staticmethod
    def from_dict(data):            #ajouter le user_Id
        return User(
            data["user_id"],
            data["nom"],
            data["prenom"],
            data["date_de_naissance"],  
            data["email"],
            data["adresse"],
            data.get("is_admin", False)  
        )

class UserManager:
    def __init__(self, json_file="users.json"):
        self.json_file = json_file
        self.users = self.load_data()
    
    def load_data(self):
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r') as file:
            return [User.from_dict(user) for user in json.load(file)]
    
    def save_data(self):
        with open(self.json_file, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file, indent=4)
    
    def add_user(self, user):
        self.users.append(user)
        self.save_data()

    def remove_user(self, user): #a verifier
        self.users.remove(user)
        self.save_data()
    
    def update_user(self, old_user, new_user): # a verifer avec l'id
        index = self.users.index(old_user)
        self.users[index] = new_user
        self.save_data()

class UserApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Utilisateurs")
        self.user_manager = UserManager()
        
        self.listbox = tk.Listbox(self.root, width=150, height=30)
        self.listbox.pack(pady=10)
        
        self.add_button = tk.Button(self.root, text="Ajouter Utilisateur", command=self.add_user_form)
        self.add_button.pack(pady=10)
        self.add_button = tk.Button(self.root, text="Modifier Utilisateur", command=self.add_user_form)
        self.add_button.pack(pady=10)
        self.add_button = tk.Button(self.root, text="Supprimer Utilisateur", command=self.add_user_form)
        self.add_button.pack(pady=10)
        
        self.update_listbox()
    
    def add_user_form(self):                

        self.form_window = tk.Toplevel(self.root) 
        self.form_window.title("Formulaire Utilisateur")

        self.form_window.geometry("700x350")

        self.user_number= User.user_number

        self.user_number_label = tk.Label(self.form_window, text="N°:")
        self.user_number_label.grid(row=0, column=0, sticky='w')
        self.user_number_entry = tk.Entry(self.form_window, state='readonly', textvariable=tk.StringVar(self.form_window, value=str(self.user_number)))  # Set user number as read-only
        self.user_number_entry.grid(row=0, column=1)
        
        self.first_name_label = tk.Label(self.form_window, text="Nom:")
        self.first_name_label.grid(row=1, column=0, sticky='w')
        self.first_name_entry = tk.Entry(self.form_window)
        self.first_name_entry.grid(row=1, column=1)
        
        self.last_name_label = tk.Label(self.form_window, text="Prénom:")
        self.last_name_label.grid(row=2, column=0, sticky='w')
        self.last_name_entry = tk.Entry(self.form_window)
        self.last_name_entry.grid(row=2, column=1)

        self.birthdate_label = tk.Label(self.form_window, text="Date de naissance:")
        self.birthdate_label.grid(row=3, column=0, sticky='w')
        self.birthdate_entry = tk.Entry(self.form_window)
        self.birthdate_entry.grid(row=3, column=1)

        self.email_label = tk.Label(self.form_window, text="Email:")
        self.email_label.grid(row=4, column=0, sticky='w')
        self.email_entry = tk.Entry(self.form_window)
        self.email_entry.grid(row=4, column=1)

        self.address_label = tk.Label(self.form_window, text="Adresse:")
        self.address_label.grid(row=5, column=0, sticky='w')
        self.adress_entry = tk.Entry(self.form_window)
        self.adress_entry.grid(row=5, column=1)

        self.is_admin_label = tk.Label(self.form_window, text="Admin ?")
        self.is_admin_label.grid(row=6, column=0, sticky='w')

        # Create a boolean variable to store the checkbutton state
        self.is_admin_var = tk.BooleanVar()
        self.is_admin_var.set(False)  # Set default to non-admin

        
        self.is_admin_checkbutton = tk.Checkbutton(self.form_window, text="Oui", variable=self.is_admin_var)
        self.is_admin_checkbutton.grid(row=6, column=1)
        
        self.submit_button = tk.Button(self.form_window, text="Valider", command=self.add_user)
        self.submit_button.grid(row=8, column=0, columnspan=2)
    
    def add_user(self):                         
        user_id = self.user_number_entry.get()
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        birthdate = self.birthdate_entry.get()
        email = self.email_entry.get()
        address = self.adress_entry.get()
        is_admin = self.is_admin_var.get()

        #gerer le message d'erreur de champs vide
        if not first_name or not last_name or not birthdate or not email or not address :
            return
        
        user = User(user_id, first_name, last_name, birthdate, email, address, is_admin)
        self.user_manager.add_user(user)
        self.update_listbox()
        self.form_window.destroy()

           
 #   def update_listbox(self):
        self.listbox.delete(0, tk.END)

        for user in self.user_manager.users:
            user_info = [
                f"Numero : {user.user_id}",
                f"Nom : {user.firstname}",
                f"Prénom : {user.lastname}",
                f"Date de naissance : {user.birthdate}",
                f"Email : {user.email}",
                f"Adresse : {user.address}",
                f"Admin : {user.is_admin}",
            ]

            # Insert user information with consistent formatting
            for item in user_info:
                self.listbox.insert(tk.END, item)
                self.listbox.itemconfig(tk.END, foreground="black")

            # Insert separator line after each user
            self.listbox.insert(tk.END, "------------------------------")
            self.listbox.itemconfig(tk.END, foreground="gray")     
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for user in self.user_manager.users:
            self.listbox.insert(tk.END, "------------------------------")
            self.listbox.insert(tk.END, f" {user.user_id} {user.firstname} {user.lastname} {user.birthdate} {user.email} {user.address} {user.is_admin}")


if __name__ == "__main__":
    root = tk.Tk()
    app = UserApp(root)
    root.mainloop()