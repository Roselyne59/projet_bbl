import tkinter as tk
from tkinter import ttk
from borrow import Borrow
from borrowManager import BorrowManager
from userManager import UserManager
from bookManager import BookManager
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
        #self.load_borrows()

        #Search borrow by user button
        self.search_label = tk.Label(self.root, text="Liste emprunts par membre")
        self.search_label.pack(pady=10)
        self.search_entry = tk.Entry(self.root)
        self.search_entry.pack(pady=10)
        self.search_button = tk.Button(self.root, text="Rechercher", command=lambda : self.search_borrow(self.tree))
        self.search_button.pack(pady=10)

        #Refresh borrow list button 
        self.refresh_list_button = tk.Button(self.root, text="Actualiser la liste", command=lambda : self.refresh_list(self.tree))
        self.refresh_list_button.pack(pady=10)

        # Treeview for displaying borrows
        self.tree = ttk.Treeview(self.root, columns=('ID_Emprunt', 'Id_Membre', 'Id_Livre', 'Date Emprunt', 'Date Retour'), show='headings')
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Define headings
        self.tree.heading('ID_Emprunt', text='ID Emprunt')
        self.tree.heading('Id_Membre', text='Id Membre')
        self.tree.heading('Id_Livre', text='Id Livre')
        self.tree.heading('Date Emprunt', text='Date Emprunt')
        self.tree.heading('Date Retour', text='Date Retour')

        # Define column widths
        self.tree.column('ID_Emprunt', width=100)
        self.tree.column('Id_Membre', width=100)
        self.tree.column('Id_Livre', width=100)
        self.tree.column('Date Emprunt', width=150)
        self.tree.column('Date Retour', width=150)

        # Frame for aligning buttons horizontally
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.add_button = tk.Button(button_frame, text="Créer Emprunt", command=self.show_borrow_form)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.modify_button = tk.Button(button_frame, text="Modifier Emprunt", command=self.modify_borrow_form)
        self.modify_button.pack(side=tk.LEFT, padx=10)

        self.delete_button = tk.Button(button_frame, text="Supprimer Emprunt", command=self.delete_borrow)
        self.delete_button.pack(side=tk.LEFT, padx=10)

        self.update_treeview(self.tree)
         
    #Refresh user list
    def refresh_list(self, treeview):
        self.update_treeview()

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

        borrow_id = borrow.borrow_id if borrow else len(self.borrow_manager.borrows) + 1

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
            user = next(user for user in self.user_manager.users if user.user_id == borrow.user_id)
            self.user_id_var.set(f"{user.user_id} - {user.firstname} {user.lastname}")

        self.book_id_label = tk.Label(self.form_window, text="Livre:")
        self.book_id_label.grid(row=2, column=0, sticky='E')
        self.book_id_var = tk.StringVar(self.form_window)
        self.book_id_menu = ttk.Combobox(self.form_window, textvariable=self.book_id_var, values=[f"{book.book_id} - {book.title}" for book in self.book_manager.books])
        self.book_id_menu.grid(row=2, column=1)
        if borrow:
            book = next(book for book in self.book_manager.books if book.book_id == borrow.book_id)
            self.book_id_var.set(f"{book.book_id} - {book.title}")

        self.start_date_label = tk.Label(self.form_window, text="Date Emprunt:")
        self.start_date_label.grid(row=3, column=0, sticky='E')
        self.start_date_entry = DateEntry(self.form_window, date_pattern='dd/mm/yyyy', selectmode='day', year=2024, month=1, day=1)
        self.start_date_entry.grid(row=3, column=1)
        self.start_date_entry.configure(width=17)
        if borrow:
            self.start_date_entry.set_date(borrow.start_date)

        self.due_date_label = tk.Label(self.form_window, text="Date Retour:")
        self.due_date_label.grid(row=4, column=0, sticky='E')
        self.due_date_entry = DateEntry(self.form_window, date_pattern='dd/mm/yyyy', selectmode='day', year=2024, month=1, day=15)
        self.due_date_entry.grid(row=4, column=1)
        self.due_date_entry.configure(width=17)
        if borrow:
            self.due_date_entry.set_date(borrow.due_date)

        self.is_approved_label = tk.Label(self.form_window, text="Approuvé:")
        self.is_approved_label.grid(row=5, column=0, sticky='E')
        self.is_approved_var = tk.BooleanVar()
        self.is_approved_var.set(borrow.is_approved if borrow else False)
        self.is_approved_checkbutton = tk.Checkbutton(self.form_window, text="Oui", variable=self.is_approved_var)
        self.is_approved_checkbutton.grid(row=5, column=1)

        self.submit_button = tk.Button(self.form_window, text="Valider", command=lambda: self.save_borrow(borrow))
        self.submit_button.grid(row=6, column=0, columnspan=2)

    def save_borrow(self, borrow):
        borrow_id = int(self.borrow_id_entry.get())
        user_id = self.user_id_var.get().split(' - ')[0]  # Extract the user_id
        book_id = self.book_id_var.get().split(' - ')[0]  # Extract the book_id
        start_date = self.start_date_entry.get_date()
        due_date = self.due_date_entry.get_date()
        is_approved = self.is_approved_var.get()

        if borrow:
            borrow.user_id = user_id
            borrow.book_id = book_id
            borrow.start_date = start_date
            borrow.due_date = due_date
            borrow.is_approved = is_approved
        else:
            new_borrow = Borrow(borrow_id, user_id, book_id, start_date, due_date, is_approved)
            self.borrow_manager.add_borrow(new_borrow)

        self.update_treeview(self.tree)  # Assuming you have a treeview widget to update
        self.form_window.destroy()
    def modify_borrow_form ():
        pass

    def delete_borrow():
        pass

    def update_treeview(self, treeview):
        for item in treeview.get_children():
            treeview.delete(item)
        for borrow in self.borrow_manager.borrows:
            treeview.insert('', 'end', values=(
                borrow.borrow_id,
                borrow.user_id,
                borrow.book_id,
                borrow.start_date,
                borrow.due_date,
                borrow.is_approved
            ))

if __name__ == "__main__":
    root = tk.Tk()
    app = BorrowApp(root)
    root.mainloop()
        