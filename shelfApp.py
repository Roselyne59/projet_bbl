import tkinter as tk
from tkinter import messagebox
from shelfManager import ShelfManager
from bookManager import BookManager
from shelf import Shelf
from book import Book

class ShelfApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Étagères")

        self.shelf_manager = ShelfManager()
        self.book_manager = BookManager()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)

        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        self.research_label = tk.Label(self.root, text="Recherche par numéro")
        self.research_label.pack(pady=10)
        self.research_entry = tk.Entry(self.root)
        self.research_entry.pack(pady=10)
        self.research_button = tk.Button(self.root, text="Recherche", command=self.research_shelf)
        self.research_button.pack(pady=10)

        self.list = tk.Listbox(self.root, width=150, height=20)
        self.list.pack(pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=10)

        self.add_button = tk.Button(button_frame, text="Ajouter une étagère", command=self.add_shelf)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.edit_button = tk.Button(button_frame, text="Modifier une étagère", command=self.edit_shelf)
        self.edit_button.pack(side=tk.LEFT, padx=10)

        self.remove_button = tk.Button(button_frame, text="Supprimer une étagère", command=self.remove_shelf)
        self.remove_button.pack(side=tk.LEFT, padx=10)

        self.add_book_button = tk.Button(button_frame, text="Ajouter un livre à l'étagère", command=self.add_book_to_shelf)
        self.add_book_button.pack(side=tk.LEFT, padx=10)

        self.update_list()

    def research_shelf(self):
        search = self.research_entry.get().strip().lower()
        filtered_shelves = [shelf for shelf in self.shelf_manager.shelves if search in str(shelf.number).lower()]
        self.show_research(filtered_shelves)

    def show_research(self, filtered_shelves):
        search_wind = tk.Toplevel(self.root)
        search_wind.title("Résultats de la recherche")

        wind_width = 700
        wind_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_x = (screen_width // 2) - (wind_width // 2)
        position_y = (screen_height // 2) - (wind_height // 2)

        search_wind.geometry(f"{wind_width}x{wind_height}+{position_x}+{position_y}")

        search_list = tk.Listbox(search_wind, width=150, height=30)
        search_list.pack(pady=10)

        for shelf in filtered_shelves:
            search_list.insert(tk.END, f"Numéro : {shelf.number}")
            search_list.insert(tk.END, f"Lettre : {shelf.letter}")
            search_list.insert(tk.END, "-----------------------------")
            
    def edit_shelf(self):
        selected_shelf_index = self.list.curselection()
        if not selected_shelf_index:
            messagebox.showwarning("Veuillez sélectionner une étagère à modifier.")
            return

        shelf_number = int(self.list.get(selected_shelf_index[0]).split(":")[1].strip())
        shelf = next((s for s in self.shelf_manager.shelves if s.number == shelf_number), None)
        self.add_shelf(shelf)

    def remove_shelf(self):
        selected_shelf_index = self.list.curselection()
        if not selected_shelf_index:
            messagebox.showwarning("Veuillez sélectionner une étagère à supprimer.")
            return

        shelf_number = int(self.list.get(selected_shelf_index[0]).split(":")[1].strip())
        self.shelf_manager.remove_shelf(shelf_number)
        self.update_list()

    def add_shelf(self, shelf=None):
        self.shelf_wind = tk.Toplevel(self.root)
        self.shelf_wind.title("Formulaire Étagère")

        wind_width = 500
        wind_height = 200
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_x = (screen_width // 2) - (wind_width // 2)
        position_y = (screen_height // 2) - (wind_height // 2)
        self.shelf_wind.geometry(f"{wind_width}x{wind_height}+{position_x}+{position_y}")

        self.number_label = tk.Label(self.shelf_wind, text="Numéro : ")
        self.number_label.grid(row=0, column=0, sticky='E')
        self.number_entry = tk.Entry(self.shelf_wind)
        self.number_entry.grid(row=0, column=1)
        self.number_entry.insert(0, shelf.number if shelf else "")
        self.number_entry.focus_set()

        self.letter_label = tk.Label(self.shelf_wind, text="Lettre : ")
        self.letter_label.grid(row=1, column=0, sticky='E')
        self.letter_entry = tk.Entry(self.shelf_wind)
        self.letter_entry.grid(row=1, column=1)
        self.letter_entry.insert(0, shelf.letter if shelf else "")

        self.submit_button = tk.Button(self.shelf_wind, text="Valider", command=lambda: self.save_shelf(shelf))
        self.submit_button.grid(row=2, column=0, columnspan=2)

    def save_shelf(self, shelf=None):
        try :
            number = int(self.number_entry.get())
        except ValueError:
            messagebox.showwarning("Attention ! Veuillez entrez un chiffre")
            return

        letter = self.letter_entry.get().strip().upper()
        if not letter.isalpha() or len(letter) != 1 :
            messagebox.showwarning("Attention ! Veuillez entrez une lettre")
            return

        if not number or not letter:
            messagebox.showwarning("Veuillez remplir tous les champs demandés !")
            return
        
        new_shelf = Shelf(Shelf.shelf_number, number, letter)
        if shelf :
            self.shelf_manager.update_shelf(shelf.number, new_shelf)
        else :
            self.shelf_manager.add_shelf(new_shelf)

        self.update_list()
        self.shelf_wind.destroy()


    def add_book_to_shelf(self):
        selected_shelf_index = self.list.curselection()
        if not selected_shelf_index :
            messagebox.showwarning("Veuillez sélectionner une étagère.")
            return
        
        shelf_number = int(self.list.get(selected_shelf_index[0]).split(":")[1].strip())
        self.book_wind = tk.Toplevel(self.root)
        self.book_wind.title("Ajouter un livre à l'étagère")

        wind_width = 500
        wind_height = 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_x = (screen_width // 2) - (wind_width // 2)
        position_y = (screen_height // 2) - (wind_height // 2)
        self.book_wind.geometry(f"{wind_width}x{wind_height}+{position_x}+{position_y}")

        self.book_id_label = tk.Label(self.book_wind, text="ID du libre : ")
        self.book_id_label.grid(row=0, column=0, sticky='E')
        self.book_id_entry = tk.Entry(self.book_wind)
        self.book_id_entry.grid(row=0, column=1)
        self.book_id_entry.focus_set()

        self.book_submit_button = tk.Button(self.book_wind, text="Valider", command=lambda: self.save_book_to_shelf(shelf_number))
        self.book_submit_button.grid(row=1, column=0, columnspan=2)

    def save_book_to_shelf(self, shelf_number):
        book_id = self.book_id_entry.get()
        if not book_id.isdigit():
            messagebox.showwarning("L'ID du livre doit être un nombre.")
            return
        book_id = int(book_id)
        book = next((b for b in self.book_manager.books if b.book_id == book_id), None)
        if not book:
            messagebox.showwarning("Livre introuvable.")
            return
        
        self.shelf_manager.add_book_to_shelf(shelf_number, book)
        self.update_list()
        self.book_wind.destroy()

    def remove_book_from_shelf(self):
        pass

    def confirm_remove_book_from_shelf(self, shelf_number):
        pass

    def update_list(self):
        self.list.delete(0, tk.END)
        for shelf in self.shelf_manager.shelves:
            self.list.insert(tk.END, f"Numéro : {shelf.number}")
            self.list.insert(tk.END, f"Letter : {shelf.letter}")
            if hasattr(self, 'books'):
                for book in shelf.books:
                    self.list.insert(tk.END, f" - {book.title} by {', '.join(book.authors)}")
            self.list.insert(tk.END, "-------------------")

if __name__ == "__main__":
    root = tk.Tk()
    app = ShelfApp(root)
    root.mainloop()