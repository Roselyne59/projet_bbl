import tkinter as tk
import re
from tkinter import messagebox
from tkcalendar import DateEntry
from book import Book
from bookManager import BookManager

class BookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des livres")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        window_width = int(screen_width * 0.8)
        window_height = int(screen_height * 0.8)

        position_x = (screen_width // 2) - (window_width // 2)
        position_y = (screen_height // 2) - (window_height // 2)

        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        self.book_manager = BookManager()

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
        title = self.research_entry.get()
        if not title:
            messagebox.showwarning("Erreur", "Veuillez entrer un titre.")
            return
        
        filtered_books = [b for b in self.book_manager.books if title.lower() in b.title.lower()]
        self.show_research(filtered_books)

    def show_research(self, filtered_books):
    #    self.list.delete(0, tk.END)
    #    for book in filtered_books:
    #        self.list.insert(tk.END, f"{book.title} by {', '.join(book.authors)} (ID : {book.book_id})")
        search_wind = tk.Toplevel(self.root)
        search_wind.title("Recherche de livre.")

        wind_width = 700
        wind_heigth = 400
        screen_width = self.root.winfo_screenwidth()
        screen_heigth = self.root.winfo_screenheight()
        position_x = (screen_width // 2) - (wind_width // 2)
        position_y = (screen_heigth // 2) - (wind_heigth // 2)

        search_wind.geometry(f"{wind_width}x{wind_heigth}+{position_x}+{position_y}")

        search_list = tk.Listbox(search_wind, width=150, height=30)
        search_list.pack(pady=10)

        for book in filtered_books :
            search_list.insert(tk.END, f"Numero : {book.book_id}")
            book_info = [
                f"Titre : {book.titile}",
                f"Auteurs : {book.authors}",
                f"Année de publication : {book.publication_year}",
                f"Isbn : {book.isbn}",
                f"Editeur : {book.editor}",
                f"Collections : {book.collections}",
                f"Genres : {book.genres}"
            ]
            for item in book_info :
                search_list.insert(tk.END, item)
            search_list.insert(tk.END, "----------------------")


    def add_book(self, book=None):
        self.form_wind = tk.Toplevel(self.root)
        self.form_wind.title("Formulaire Livres")

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
        self.authors_entry.insert(0, book.authors if book else " ")


        validate_year_cmd = (self.form_wind.register(self.validate_year), '%P') 
        
        self.publi_year_label = tk.Label(self.form_wind, text="Année de publication : ")
        self.publi_year_label.grid(row=3, column=0, sticky='E')
        self.publi_year_entry = tk.Entry(self.form_wind, validate="key", validatecommand=validate_year_cmd)
        self.publi_year_entry.grid(row=3, column=1)
        self.publi_year_entry.configure(width=17)
        if book:
            self.publi_year_entry.insert(0, str(book.publication.year))
        

        validate_num_cmd = (self.form_wind.register(self.validate_number), '%P')

        self.numb_label = tk.Label(self.form_wind, text="ISBN : ")
        self.numb_label.grid(row=4, column=0)
        self.numb_entry = tk.Entry(self.form_wind, validate="key", validatecommand=validate_num_cmd)
        self.numb_entry.grid(row=4, column=1)
        self.numb_entry.configure(width=17)

        self.editor_label = tk.Label(self.form_wind, text="Editeur(s) : ")
        self.editor_label.grid(row=5, column=0)
        self.editor_list = tk.Listbox(self.form_wind, selectmode=tk.MULTIPLE)
        self.editor_list.grid(row=5, column=1)
        for editor in ["Editor 1", "Editor 2", "Editor 3"]:
            self.editor_list.insert(tk.END, editor)

        self.coll_label = tk.Label(self.form_wind, text="Collection(s) : ")
        self.coll_label.grid(row=6, column=0)
        self.coll_list= tk.Listbox(self.form_wind, selectmode=tk.MULTIPLE)
        self.coll_list.grid(row=6, column=1)
        for collection in ["Collection 1", "Collection 2", "Collection 3"]:
            self.coll_list.insert(tk.END, collection)

        self.genre_label = tk.Label(self.form_wind, text="Genre(s) : ")
        self.genre_label.grid(row=5, column=0)
        self.genre_list = tk.Listbox(self.form_wind, selectmode=tk.MULTIPLE)
        self.genre_list.grid(row=5, column=1)
        for genre in ["Genre 1", "Genre 2", "Genre 3"]:
            self.genre_list.insert(tk.END, genre)

        self.submit_button = tk.Button(self.form_wind, text="Valider", command=lambda: self.save_book(book))
        self.submit_button.grid(row=6, column=0, columnspan=0)

    def validate_title(self, value):
        if re.match(r'^[A-Z][a-z]*$', value) :
            return True
        else :
            return False
        
    def validate_year(self, value):
        if re.match(r'^\d{0,4}$', value):
            return True
        else:
            return False
        
    def validate_number(self, value):
        if re.match(r'^\d{0,13}$', value):
            return True
        else:
            return False
        
    def save_book(self, book=None):
        book_id = int(self.book_id_entry.get())
        title = self.title_entry.get()
        authors = self.authors_entry.get()
        publication_year = self.publi_year_entry.get()
        isbn = self.numb_entry.get()
        editor = self.editor_list.get()
        collections = self.coll_list.get()
        genres = self.genre_list.get()

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



    def update_list(self):
        self.list.delete(0, tk.END)
        for book in self.book_manager.books:
        #    self.list.insert(tk.END, f"{book.title} by {', '.join(book.authors)} (ID: {book.book_id})")
            self.list.insert(tk.END, f"Numéro : {book.book_id}")
            book_info = [
                f"Titre : {book.titile}",
                f"Auteurs : {book.authors}",
                f"Année de publication : {book.publication_year}",
                f"Isbn : {book.isbn}",
                f"Editeur : {book.editor}",
                f"Collections : {book.collections}",
                f"Genres : {book.genres}"
            ]
            for item in book_info :
                self.list.insert(tk.END, item)
            self.list.insert(tk.END, "-----------------------")