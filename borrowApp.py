import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from borrow import Borrow
from borrowManager import BorrowManager
from userManager import UserManager
from bookManager import BookManager
from tkcalendar import DateEntry

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
        self.search_button = tk.Button(self.root, text="Rechercher", font=('Helvetica', 10, 'bold'), command=lambda : self.search_borrow(self.tree))
        self.search_button.pack(pady=10)

        #Refresh borrow list button 
        self.refresh_list_button = tk.Button(self.root, text="Actualiser la liste", font=('Helvetica', 10, 'bold'), command=lambda : self.refresh_list(self.tree))
        self.refresh_list_button.pack(pady=10)

        # Treeview for displaying borrows
        self.tree = ttk.Treeview(self.root, columns=('ID_Emprunt', 'Id_Membre', 'Nom Utilisateur', 'Id_Livre', 'Titre Livre', 'Date Emprunt', 'Date Retour'), show='headings')
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Define headings
        self.tree.heading('ID_Emprunt', text='ID Emprunt')
        self.tree.heading('Id_Membre', text='Id Membre')
        self.tree.heading('Nom Utilisateur', text='Nom Utilisateur')
        self.tree.heading('Id_Livre', text='Id Livre')
        self.tree.heading('Titre Livre', text='Titre Livre')
        self.tree.heading('Date Emprunt', text='Date Emprunt')
        self.tree.heading('Date Retour', text='Date Retour')

        # Define column widths
        self.tree.column('ID_Emprunt', width=100)
        self.tree.column('Id_Membre', width=100)
        self.tree.column('Nom Utilisateur', width=150)
        self.tree.column('Id_Livre', width=100)
        self.tree.column('Titre Livre', width=150)
        self.tree.column('Date Emprunt', width=150)
        self.tree.column('Date Retour', width=150)

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
        self.book_id_menu = ttk.Combobox(self.form_window, textvariable=self.book_id_var, values=self.get_available_books())
        self.book_id_menu.grid(row=2, column=1)
        if borrow:
            book = next(book for book in self.book_manager.books if book.book_id == borrow.book_id)
            self.book_id_var.set(f"{book.book_id} - {book.title}")

        self.start_date_label = tk.Label(self.form_window, text="Date Emprunt:")
        self.start_date_label.grid(row=3, column=0, sticky='E')
        self.start_date_entry = DateEntry(self.form_window, date_pattern='dd/mm/yyyy', selectmode='day', year=2024, month=1, day=1)
        self.start_date_entry.grid(row=3, column=1)
        self.start_date_entry.configure(width=20)
        if borrow:
            self.start_date_entry.set_date(borrow.start_date)

        self.due_date_label = tk.Label(self.form_window, text="Date Retour:")
        self.due_date_label.grid(row=4, column=0, sticky='E')
        self.due_date_entry = DateEntry(self.form_window, date_pattern='dd/mm/yyyy', selectmode='day', year=2024, month=1, day=1)
        self.due_date_entry.grid(row=4, column=1)
        self.due_date_entry.configure(width=20)
        if borrow:
            self.due_date_entry.set_date(borrow.due_date)

        self.submit_button = tk.Button(self.form_window, text="Valider", font=('Helvetica', 10, 'bold'), command=lambda: self.save_borrow(borrow))
        self.submit_button.grid(row=8, column=0, columnspan=2)

    def get_available_books(self):
        # Filtrer les livres disponibles
        available_books = [book for book in self.book_manager.books if book.is_available]
        return [f"{book.book_id} - {book.title}" for book in available_books]

    def save_borrow(self, borrow):
        borrow_id = int(self.borrow_id_entry.get())
        user_info = self.user_id_var.get().split(' - ')
        user_id = user_info[0]
        user_name = user_info[1]  # Assuming user name is the second part after splitting

        book_info = self.book_id_var.get().split(' - ')
        book_id = book_info[0]
        book_title = book_info[1]  # Assuming book title is the second part after splitting

        start_date = self.start_date_entry.get_date().strftime('%Y-%m-%d')
        due_date = self.due_date_entry.get_date().strftime('%Y-%m-%d')

        # Vérifier si le livre est disponible
        book = next((b for b in self.book_manager.books if b.book_id == book_id), None)
        if book and not book.is_available:
            messagebox.showerror("Erreur", f"Le livre '{book.title}' n'est pas disponible.")
            return

        if borrow:
            # Update existing borrow details
            borrow.user_id = user_id
            borrow.user_name = user_name
            borrow.book_id = book_id
            borrow.book_title = book_title
            borrow.start_date = start_date
            borrow.due_date = due_date
        else:
            # Create new borrow
            new_borrow = Borrow(borrow_id, user_id, user_name, book_id, book_title, start_date, due_date)
            self.borrow_manager.add_borrow(new_borrow)
            # Mark the book as unavailable
            book = next((b for b in self.book_manager.books if b.book_id == book_id), None)
            if book:
                book.is_available = False  # Mark the book as unavailable

        self.update_treeview(self.tree)  # Assuming you have a treeview widget to update
        self.form_window.destroy()

    def modify_borrow_form ():
        pass

    def delete_borrow(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Attention", "Veuillez sélectionner un emprunt à supprimer.")
            return
        selected_borrow_id = self.tree.item(selected_item[0])['values'][0]
        self.borrow_manager.remove_borrow(selected_borrow_id)
        self.update_treeview(self.tree)

    def update_treeview(self, treeview):
        for item in treeview.get_children():
            treeview.delete(item)
        for borrow in self.borrow_manager.borrows:
            treeview.insert('', 'end', values=(
                borrow.borrow_id,
                borrow.user_id,
                borrow.user_name,
                borrow.book_id,
                borrow.book_title,
                borrow.start_date,
                borrow.due_date,
            ))

if __name__ == "__main__":
    root = tk.Tk()
    app = BorrowApp(root)
    root.mainloop()