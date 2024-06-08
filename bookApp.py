import tkinter as tk
from tkinter import messagebox, simpledialog
from tkcalendar import DateEntry
from book import Book
from bookManager import BookManager

class BookApp:
    def __init__(self, root, book_manager):
        self.root = root
        self.root.title("Gestion des livres")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)

        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        self.book_manager = book_manager

        self.research_label = tk.Label(self.root, text="Recherche par titre")
        self.research_label.pack(pady=10)
        self.research_entry = tk.Entry(self.root)
        self.research_entry.pack(pady=10)
        self.research_button = tk.Button(self.root, text="Recherche", command=self.research_book)
        self.research_button.pack(pady=10)

        self.list = tk.Listbox(self.root, width=150, height=20)
        self.list.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.add_button = tk.Button(button_frame, text="Ajouter un livre", command=self.show_book)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.edit_button = tk.Button(button_frame, text="Modifier un livre", command=self.edit_book)
        self.edit_button.pack(side=tk.LEFT, padx=10)

        self.remove_button = tk.Button(button_frame, text="Supprimer un livre", command=self.remove_book)
        self.remove_button.pack(side=tk.LEFT, padx=10)

        self.add_wishlist_button = tk.Button(button_frame, text="Ajouter à la wishlist", command=self.add_to_wishlist)
        self.add_wishlist_button.pack(side=tk.LEFT, padx=10)

        self.view_wishlist_button = tk.Button(button_frame, text="Voir la wishlist", command=self.view_wishlist)
        self.view_wishlist_button.pack(side=tk.LEFT, padx=10)

        self.update_list()

    def research_book(self):
        title = self.research_entry.get()
        if not title:
            messagebox.showwarning("Erreur", "Veuillez entrer un titre.")
            return
        
        filtered_books = [b for b in self.book_manager.books if title.lower() in b.title.lower()]
        self.show_research(filtered_books)

    def show_research(self, filtered_books):
        self.list.delete(0, tk.END)
        for book in filtered_books:
            self.list.insert(tk.END, f"{book.title} by {', '.join(book.authors)} (ID : {book.book_id})")

    def show_book(self, book=None):
        pass

    def edit_book(self):
        selected_book_index = self.list.curselection()
        if not selected_book_index:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner un livre à modifier.")
            return
        
        book_id = int(self.list.get(selected_book_index[0]).split(":")[1].strip())
        book = next((b for b in self.book_manager.books if b.book_id == book_id), None)

        self.show_book(book)

    def remove_book(self):
        selected_book_index = self.list.curselection()
        if not selected_book_index:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner un livre à supprimer.")
            return

        book_id = int(self.list.get(selected_book_index[0]).split(":")[1].strip())
        self.book_manager.remove_book(book_id)
        self.update_list()

    def add_to_wishlist(self):
        selected_book_index = self.list.curselection()
        if not selected_book_index:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner un livre à ajouter à la wishlist.")
            return

        book_id = int(self.list.get(selected_book_index[0]).split(":")[1].strip())
        book = next((b for b in self.book_manager.books if b.book_id == book_id), None)
        self.book_manager.add_book_to_wishlist(book)
        messagebox.showinfo("Succès", "Livre ajouté à la wishlist.")

    def view_wishlist(self):
        wishlist_window = tk.Toplevel(self.root)
        wishlist_window.title("Wishlist")

        wishlist_listbox = tk.Listbox(wishlist_window, width=100, height=20)
        wishlist_listbox.pack(pady=10)

        for book in self.book_manager.get_wishlist():
            wishlist_listbox.insert(tk.END, str(book))

        remove_button = tk.Button(wishlist_window, text="Supprimer de la wishlist", command=lambda: self.remove_from_wishlist(wishlist_listbox))
        remove_button.pack(pady=10)

    def remove_from_wishlist(self, listbox):
        selected_book_index = listbox.curselection()
        if not selected_book_index:
            messagebox.showwarning("Avertissement", "Veuillez sélectionner un livre à supprimer de la wishlist.")
            return

        book_id = int(listbox.get(selected_book_index[0]).split(":")[1].strip())
        self.book_manager.remove_book_from_wishlist(book_id)
        listbox.delete(selected_book_index)

    def update_list(self):
        self.list.delete(0, tk.END)
        for book in self.book_manager.books:
            self.list.insert(tk.END, f"{book.title} by {', '.join(book.authors)} (ID: {book.book_id})")
