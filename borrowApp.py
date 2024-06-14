import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from borrow import Borrow
from borrowManager import BorrowManager
from userManager import UserManager
from bookManager import BookManager
from tkcalendar import DateEntry
from datetime import datetime

class BorrowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Emprunts")

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

        self.borrow_manager = BorrowManager()
        self.book_manager = BookManager()
        self.user_manager = UserManager()
        

        #Search borrow by user button
        self.search_label = tk.Label(self.root, text="Liste emprunts par membre", font=('Helvetica', 10, 'bold'))
        self.search_label.pack(pady=10)

        self.search_user_var = tk.StringVar()
        self.search_combobox = ttk.Combobox(self.root, textvariable=self.search_user_var)
        self.search_combobox.pack(pady=10)
        self.search_combobox['values'] = [f"{user.user_id} - {user.firstname} {user.lastname}" for user in self.user_manager.users]
        self.search_button = tk.Button(self.root, text="Rechercher", font=('Helvetica', 10, 'bold'), command=lambda : self.search_borrow_by_user())
        self.search_button.pack(pady=10)

        #Refresh borrow list button 
        self.refresh_list_button = tk.Button(self.root, text="Actualiser la liste", font=('Helvetica', 10, 'bold'), command=lambda : self.refresh_list(self.tree))
        self.refresh_list_button.pack(pady=10)

        # Treeview for displaying borrows
        self.tree = ttk.Treeview(self.root, columns=('ID_Emprunt', 'Id_Membre', 'Nom Utilisateur', 'Id_Livre', 'Titre Livre', 'Date Emprunt', 'Date Retour', 'Retard en jours', 'Montant Amende'), show='headings')
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Define headings
        self.tree.heading('ID_Emprunt', text='ID Emprunt')
        self.tree.heading('Id_Membre', text='Id Membre')
        self.tree.heading('Nom Utilisateur', text='Nom Utilisateur')
        self.tree.heading('Id_Livre', text='Id Livre')
        self.tree.heading('Titre Livre', text='Titre Livre')
        self.tree.heading('Date Emprunt', text='Date Emprunt')
        self.tree.heading('Date Retour', text='Date Retour')
        self.tree.heading('Retard en jours', text='Retard en jours')
        self.tree.heading('Montant Amende', text='Montant Amende en €')

        # Define column widths
        self.tree.column('ID_Emprunt', width=50, anchor=tk.CENTER)
        self.tree.column('Id_Membre', width=50, anchor=tk.CENTER)
        self.tree.column('Nom Utilisateur', width=150, anchor=tk.CENTER)
        self.tree.column('Id_Livre', width=50, anchor=tk.CENTER)
        self.tree.column('Titre Livre', width=150, anchor=tk.CENTER)
        self.tree.column('Date Emprunt', width=80, anchor=tk.CENTER)
        self.tree.column('Date Retour', width=80, anchor=tk.CENTER)
        self.tree.column('Retard en jours', width=80, anchor=tk.CENTER)
        self.tree.column('Montant Amende', width=80, anchor=tk.CENTER)

        
        # Frame for aligning buttons horizontally
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.add_button = tk.Button(button_frame, text="Créer Emprunt", font=('Helvetica', 10, 'bold'), command=self.show_borrow_form)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.modify_button = tk.Button(button_frame, text="Modifier Emprunt", font=('Helvetica', 10, 'bold'), command=self.modify_borrow_form)
        self.modify_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(button_frame, text="Supprimer Emprunt", font=('Helvetica', 10, 'bold'), command=self.delete_borrow)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        self.update_treeview(self.tree)
         
    
    def show_borrow_form(self, borrow=None):
        self.form_window = tk.Toplevel(self.root)
        self.form_window.title("Formulaire Emprunt")

        window_width = 700
        window_height = 350

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        self.form_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        if borrow is None:
            borrow_id = len(self.borrow_manager.borrows) + 1
        else:
            borrow_id = borrow.borrow_id

        self.borrow_id_label = tk.Label(self.form_window, text="ID Emprunt:")
        self.borrow_id_label.grid(row=0, column=0, sticky='E')
        self.borrow_id_entry = tk.Entry(self.form_window, state='readonly', textvariable=tk.StringVar(self.form_window, value=str(borrow_id)))
        self.borrow_id_entry.grid(row=0, column=1)

        self.user_id_label = tk.Label(self.form_window, text="Utilisateur:")
        self.user_id_label.grid(row=1, column=0, sticky='E')
        self.user_id_var = tk.StringVar(self.form_window)
        self.user_id_menu = ttk.Combobox(self.form_window, textvariable=self.user_id_var, values=[f"{user.user_id} - {user.firstname} {user.lastname}" for user in self.user_manager.users])
        self.user_id_menu.grid(row=1, column=1)
        if borrow:
            user = next((user for user in self.user_manager.users if user.user_id == borrow.user_id), None)
            if user:
                self.user_id_var.set(f"{user.user_id} - {user.firstname} {user.lastname}")
            else:
                messagebox.showerror("Erreur", "Utilisateur non trouvé.")
                self.form_window.destroy()
                return

        self.book_id_label = tk.Label(self.form_window, text="Livre:")
        self.book_id_label.grid(row=2, column=0, sticky='E')
        self.book_id_var = tk.StringVar(self.form_window)
        self.book_id_menu = ttk.Combobox(self.form_window, textvariable=self.book_id_var, values=self.get_available_books())
        self.book_id_menu.grid(row=2, column=1)
        if borrow:
            book = next((book for book in self.book_manager.books if book.book_id == borrow.book_id), None)
            if book:
                self.book_id_var.set(f"{book.book_id} - {book.title}")
            else:
                messagebox.showerror("Erreur", "Livre non trouvé.")
                self.form_window.destroy()
                return

        self.start_date_label = tk.Label(self.form_window, text="Date Emprunt:")
        self.start_date_label.grid(row=3, column=0, sticky='E')
        self.start_date_entry = DateEntry(self.form_window, date_pattern='dd/mm/yyyy', selectmode='day')
        self.start_date_entry.grid(row=3, column=1)
        self.start_date_entry.configure(width=20)
        self.start_date_entry.set_date(datetime.now())
        if borrow:
            self.start_date_entry.set_date(borrow.start_date)

        self.due_date_label = tk.Label(self.form_window, text="Date Retour:")
        self.due_date_label.grid(row=4, column=0, sticky='E')
        self.due_date_entry = DateEntry(self.form_window, date_pattern='dd/mm/yyyy', selectmode='day')
        self.due_date_entry.grid(row=4, column=1)
        self.due_date_entry.configure(width=20)
        self.due_date_entry.set_date(datetime.now())
        if borrow:
            self.due_date_entry.set_date(borrow.due_date)

        self.submit_button = tk.Button(self.form_window, text="Valider", font=('Helvetica', 10, 'bold'), command=lambda: self.save_borrow(borrow))
        self.submit_button.grid(row=8, column=0, columnspan=2)

    def get_available_books(self):
        available_books = [book for book in self.book_manager.books if book.is_available]
        return [f"{book.book_id} - {book.title}" for book in available_books]

    def save_borrow(self, borrow):
        borrow_id = int(self.borrow_id_entry.get())
        user_info = self.user_id_var.get().split(' - ')
        user_id = user_info[0]
        user_name = user_info[1]

        book_info = self.book_id_var.get().split(' - ')
        book_id = book_info[0]
        book_title = book_info[1] 

        start_date = self.start_date_entry.get_date().strftime('%Y-%m-%d')
        due_date = self.due_date_entry.get_date().strftime('%Y-%m-%d')

        # Check if selected start date is not earlier than actual date
        today_date = datetime.now().strftime('%Y-%m-%d')
        if start_date < today_date:
            messagebox.showerror("Attention", "La date de début de l'emprunt ne peut pas être antérieure à la date d'aujourd'hui.")
            return

        # Check if book is availble
        book = next((b for b in self.book_manager.books if b.book_id == book_id), None)
        if book and not book.is_available:
            messagebox.showerror("Erreur", f"Le livre '{book.title}' n'est pas disponible.")
            return

        if borrow:
            
            borrow.user_id = user_id
            borrow.user_name = user_name
            borrow.book_id = book_id
            borrow.book_title = book_title
            borrow.start_date = start_date
            borrow.due_date = due_date
        else:
            # create new borrow
            new_borrow = Borrow(borrow_id, user_id, user_name, book_id, book_title, start_date, due_date)
            self.borrow_manager.add_borrow(new_borrow)
            # book marqued as unavailble 
            book = next((b for b in self.book_manager.books if b.book_id == book_id), None)
            if book:
                book.is_available = False

        self.update_treeview(self.tree)  
        self.form_window.destroy()

    def modify_borrow_form(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Attention", "Veuillez sélectionner un emprunt à modifier.")
            return
        
        selected_borrow_id = self.tree.item(selected_item[0])['values'][0]
        borrow = next((b for b in self.borrow_manager.borrows if b.borrow_id == selected_borrow_id), None)
        if borrow:
            print(f"Debug: Emprunt sélectionné trouvé: {borrow}")  # Debug message
            self.show_borrow_form(borrow)
        else:
            messagebox.showerror("Erreur", f"Impossible de trouver l'emprunt avec l'ID {selected_borrow_id}.")

    def delete_borrow(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Attention", "Veuillez sélectionner un emprunt à supprimer.")
            return
        selected_borrow_id = self.tree.item(selected_item[0])['values'][0]
        self.borrow_manager.remove_borrow(selected_borrow_id)
        self.update_treeview(self.tree)
    
    def search_borrow_by_user (self):
        selected_user = self.search_user_var.get().split(' - ')[0]
               
        filtered_borrows = [borrow for borrow in self.borrow_manager.borrows if borrow.user_id == selected_user]
        
        # Reset tree content
        for item in self.tree.get_children():
           self.tree.delete(item)
                
        # Display search result
        for borrow in filtered_borrows:
            #Calculate days late
            due_date = datetime.strptime(borrow.due_date, '%Y-%m-%d')
            return_date = datetime.strptime(datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
            
            days_delayed = (return_date - due_date).days
            if days_delayed < 0:
                days_delayed = 0
        
            amount_to_pay = days_delayed * 0.20 # 0.20€ per day

            self.tree.insert('', 'end', values=(
                borrow.borrow_id,
                borrow.user_id,
                borrow.user_name,
                borrow.book_id,
                borrow.book_title,
                borrow.start_date,
                borrow.due_date,
                days_delayed,
                amount_to_pay,

            ))

    #Refresh borrow list after search
    def refresh_list(self, treeview):
        self.update_treeview(treeview)

    def update_treeview(self, treeview):
        for item in treeview.get_children():
            treeview.delete(item)
        for borrow in self.borrow_manager.borrows:
            
            #Calculate days late
            due_date = datetime.strptime(borrow.due_date, '%Y-%m-%d')
            return_date = datetime.strptime(datetime.now().strftime('%Y-%m-%d'), '%Y-%m-%d')
            
            days_delayed = (return_date - due_date).days
            if days_delayed < 0:
                days_delayed = 0
        
            amount_to_pay = days_delayed * 0.20 # 0.20€ per day 
            treeview.insert('', 'end', values=(
                borrow.borrow_id,
                borrow.user_id,
                borrow.user_name,
                borrow.book_id,
                borrow.book_title,
                borrow.start_date,
                borrow.due_date,
                days_delayed,
                amount_to_pay,
            ))

if __name__ == "__main__":
    root = tk.Tk()
    app = BorrowApp(root)
    root.mainloop()