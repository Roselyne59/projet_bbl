import tkinter as tk
import re
from tkinter import messagebox
from book import Book
from bookManager import BookManager

class BookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des livres")

        self.book_manager = BookManager()

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)

        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

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

        self.add_button = tk.Button(button_frame, text="Ajouter un livre", command=self.add_book)
        self.add_button.pack(side=tk.LEFT, padx=10)

        self.edit_button = tk.Button(button_frame, text="Modifier un livre", command=self.edit_book)
        self.edit_button.pack(side=tk.LEFT, padx=10)

        self.remove_button = tk.Button(button_frame, text="Supprimer un livre", command=self.remove_book)
        self.remove_button.pack(side=tk.LEFT, padx=10)

        self.update_list()

    def research_book(self):
        search = self.research_entry.get().strip().lower()
        filtered_books = [book for book in self.book_manager.books if search in book.title.lower()]
        self.show_research(filtered_books)

    def show_research(self, filtered_books):
        search_wind = tk.Toplevel(self.root)
        search_wind.title("Resultats de la recherche")

        wind_width = 700
        wind_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_x = (screen_width // 2) - (wind_width // 2)
        position_y = (screen_height // 2) - (wind_height // 2)

        search_wind.geometry(f"{wind_width}x{wind_height}+{position_x}+{position_y}")

        search_list = tk.Listbox(search_wind, width=150, height=30)
        search_list.pack(pady=10)

        for book in filtered_books :
            search_list.insert(tk.END, f"Numero : {book.book_id}")
            book_info = [
                f"Titre : {book.title}",
                f"Auteurs : {', '.join(book.authors)}",
                f"Année de publication : {book.publication_year}",
                f"ISBN : {book.isbn}",
                f"Editeur : {book.editor}",
                f"Collections : {', '.join(book.collections)}",
                f"Genres : {', '.join(book.genres)}"
            ]
            for item in book_info :
                search_list.insert(tk.END, item)
            search_list.insert(tk.END, "----------------------------")

    def edit_book(self):
        selected_book_index = self.list.curselection()
        if not selected_book_index:
            messagebox.showwarning("Veuillez entrer un livre à modifier.")
            return
        
        book_id = int(self.list.get(selected_book_index[0]).split(":")[1].strip())
        book = next((b for b in self.book_manager.books if b.book_id == book_id), None)

        self.add_book(book)

    def remove_book(self):
        selected_book_index = self.list.curselection()
        if not selected_book_index:
            messagebox.showwarning("Veuillez entrer un livre à supprimer.")
            return

        book_id = int(self.list.get(selected_book_index[0]).split(":")[1].strip())
        self.book_manager.remove_book(book_id)
        self.update_list()


    def add_book(self, book=None):
        self.form_wind = tk.Toplevel(self.root)
        self.form_wind.title("Formulaire Livre")

        wind_width = 700
        wind_height = 350

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        position_x = (screen_width // 2) - (wind_width // 2)
        position_y = (screen_height // 2) - (wind_height // 2)

        self.form_wind.geometry(f"{wind_width}x{wind_height}+{position_x}+{position_y}")

        book_id = book.book_id if book else Book.book_number

        self.book_id_label = tk.Label(self.form_wind, text="N° : ")
        self.book_id_label.grid(row=0, column=0, sticky='E')
        self.book_id_entry = tk.Entry(self.form_wind, state="readonly", textvariable=tk.StringVar(self.form_wind, value=str(book_id)))
        self.book_id_entry.grid(row=0, column=0)


        validate_cmd = (self.form_wind.register(self.validate_title), '%P')

        self.title_label = tk.Label(self.form_wind, text="Titre : ")
        self.title_label.grid(row=1, column=0, sticky='E')
        self.title_entry = tk.Entry(self.form_wind, validate="key", validatecommand=validate_cmd)
        self.title_entry.grid(row=1, column=1)
        self.title_entry.insert(0, book.title if book else " ")
        self.title_entry.focus_set()

        self.authors_label = tk.Label(self.form_wind, text="Auteurs : ")
        self.authors_label.grid(row= 2, column=0, sticky='E')
        self.authors_entry = tk.Entry(self.form_wind)
        self.authors_entry.grid(row=2, column=1)
        self.authors_entry.insert(0, ", ".join(book.authors) if book else " ")

        validate_year_cmd = (self.form_wind.register(self.validate_year), '%P') 
        
        self.publi_year_label = tk.Label(self.form_wind, text="Année de publication : ")
        self.publi_year_label.grid(row=3, column=0, sticky='E')
        self.publi_year_entry = tk.Entry(self.form_wind, validate="key", validatecommand=validate_year_cmd)
        self.publi_year_entry.grid(row=3, column=1)
        self.publi_year_entry.insert(0, str(book.publication_year) if book else " ")

        validate_num_cmd = (self.form_wind.register(self.validate_number), '%P')

        self.numb_label = tk.Label(self.form_wind, text="ISBN : ")
        self.numb_label.grid(row=4, column=0, sticky='E')
        self.numb_entry = tk.Entry(self.form_wind, validate="key", validatecommand=validate_num_cmd)
        self.numb_entry.grid(row=4, column=1)
        self.numb_entry.insert(0, book.isbn if book else " ")

        self.editor_label = tk.Label(self.form_wind, text="Editeur(s) : ")
        self.editor_label.grid(row=5, column=0, sticky='E')
        self.editor_entry = tk.Entry(self.form_wind)
        self.editor_entry.grid(row=5, column=1)
        self.editor_entry.insert(0, book.editor if book else " ")

        self.coll_label = tk.Label(self.form_wind, text="Collection(s) : ")
        self.coll_label.grid(row=6, column=0, sticky='E')
        self.coll_entry= tk.Entry(self.form_wind)
        self.coll_entry.grid(row=6, column=1)
        self.coll_entry.insert(0, ", ".join(book.collections) if book else " ")

        self.genre_label = tk.Label(self.form_wind, text="Genre(s) : ")
        self.genre_label.grid(row=7, column=0, sticky='E')
        self.genre_list = tk.Listbox(self.form_wind, selectmode=tk.MULTIPLE)
        self.genre_list.grid(row=7, column=1)
        for genre in self.book_manager.genres:
            self.genre_list.insert(tk.END, genre)
        if book:
            for genre in book.genres:
                i = self.book_manager.genres.index(genre)
                self.genre_list.select_set(i)

        self.submit_button = tk.Button(self.form_wind, text="Valider", command=lambda: self.save_book(book))
        self.submit_button.grid(row=8, column=0, columnspan=2)

    def validate_title(self, value):
        if value == "":
            return True
        return bool(re.match(r'^[A-Z].*$', value))
        
    def validate_year(self, value):
        return bool(re.match(r'^\d{0,4}$', value))
        
    def validate_number(self, value):
        return bool(re.match(r'^\d{0,13}$', value))
        
    def save_book(self, book=None):
        book_id = int(self.book_id_entry.get())
        title = self.title_entry.get()
        authors = self.authors_entry.get().split(", ")
        publication_year_str = self.publi_year_entry.get()
        if not publication_year_str.isdigit():
            messagebox.showwarning("L'année de publication doit être un nombre.")
            return
        publication_year = int(publication_year_str)
        isbn_str = self.numb_entry.get()
        if not isbn_str.isdigit():
            messagebox.showwarning("Le numéro ISBN doit être composer de 13 chiffres.")
            return
        isbn = int(isbn_str)
        editor = self.editor_entry.get()
        collections = self.coll_entry.get().split(", ")
        genres = [self.genre_list.get(i) for i in self.genre_list.curselection()]

        if not all([title, authors, publication_year, isbn, editor, collections, genres]):
            messagebox.showwarning("Veuillez remplir tous les champs !")
            return
        
        new_book = Book(book_id, title, authors, publication_year, isbn, editor, collections, genres)

        if book:
            self.book_manager.update_book(new_book)
        else:
            self.book_manager.add_book(new_book)

        self.update_list()
        self.form_wind.destroy()

    def update_list(self):
        self.list.delete(0, tk.END)
        for book in self.book_manager.books:
            self.list.insert(tk.END, f"Numéro : {book.book_id}")
            book_info = [
                f"Titre : {book.title}",
                f"Auteurs : {', '.join(book.authors)}",
                f"Année de publication : {book.publication_year}",
                f"ISBN : {book.isbn}",
                f"Editeur : {book.editor}",
                f"Collections : {', '.join(book.collections)}",
                f"Genres : {','.join(book.genres)}"
            ]
            for item in book_info :
                self.list.insert(tk.END, item)
            self.list.insert(tk.END, "--------------------------")