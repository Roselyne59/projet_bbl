import tkinter as tk
from tkinter.ttk import Treeview
import re
from tkinter import messagebox, Label, Entry, Button, Toplevel, Listbox, Frame, StringVar, BooleanVar, Checkbutton, END, LEFT, MULTIPLE, BOTH
from book import Book
from bookManager import BookManager

class BookApp:
    def __init__(self, root) :
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

        search_frame = Frame(self.root)
        search_frame.pack(pady=10)
        
        self.title_search_frame = Frame(search_frame)
        self.title_search_frame.grid(row=0, column=0, padx=10)
        self.research_label_title = Label(self.title_search_frame, font=('Verdana', 12, 'bold'), text="Recherche par titre")
        self.research_label_title.pack(side=LEFT)
        self.research_entry_title = Entry(self.title_search_frame)
        self.research_entry_title.pack(side=LEFT)
        self.research_button = Button(self.title_search_frame, text="Recherche", font=('Verdana', 12, 'bold'), command = self.research_book_by_title)
        self.research_button.pack(side=LEFT)

        self.isbn_search_frame = Frame(search_frame)
        self.isbn_search_frame.grid(row=0, column=1, padx=10)
        self.research_label_isbn = Label(self.isbn_search_frame, font=('Verdana', 12, 'bold'), text="Recherche par numéro ISBN")
        self.research_label_isbn.pack(side=LEFT)
        self.research_entry_isbn = Entry(self.isbn_search_frame)
        self.research_entry_isbn.pack(side=LEFT)
        self.research_button = Button(self.isbn_search_frame, text="Recherche", font=('Verdana', 12, 'bold'), command = self.research_book_by_isbn)
        self.research_button.pack(side=LEFT)

        self.authors_search_frame = Frame(search_frame)
        self.authors_search_frame.grid(row=0, column=2, padx=10)
        self.research_label_authors = Label(self.authors_search_frame, font=('Verdana', 12, 'bold'), text="Recherche par auteurs")
        self.research_label_authors.pack(side=LEFT)
        self.research_entry_authors = Entry(self.authors_search_frame)
        self.research_entry_authors.pack(side=LEFT)
        self.research_button = Button(self.authors_search_frame, text="Recherche", font=('Verdana', 12, 'bold'), command = self.research_book_by_authors)
        self.research_button.pack(side=LEFT)

        self.refresh_list_button = Button(self.root, text="Actualiser la liste", font=('Verdana', 12, 'bold'), command = self.refresh_list)
        self.refresh_list_button.pack(pady=10)

        self.tree = Treeview(self.root, columns=('ID', 'Titre', 'Auteurs', 'Année de publication', 'Numéro ISBN', 'Editeurs', 'Collections', 'Genres', 'Disponibilité'), show='headings')
        self.tree.pack(pady=10, fill=BOTH, expand=True)


        self.tree.heading('ID', text='ID')
        self.tree.heading('Titre', text='Titre')
        self.tree.heading('Auteurs', text='Auteurs')
        self.tree.heading('Année de publication', text='Année de publication')
        self.tree.heading('Numéro ISBN', text='Numéro ISBN')
        self.tree.heading('Editeurs', text='Editeurs')
        self.tree.heading('Collections', text='Collections')
        self.tree.heading('Genres', text='Genres')
        self.tree.heading('Disponibilité', text='Disponibilité')

        self.tree.column('ID', width=50)
        self.tree.column('Titre', width=200)
        self.tree.column('Auteurs', width=150)
        self.tree.column('Année de publication', width=150)
        self.tree.column('Numéro ISBN', width=100)
        self.tree.column('Editeurs', width=200)
        self.tree.column('Collections', width=150)
        self.tree.column('Genres', width=150)
        self.tree.column('Disponibilité', width=100)


        button_frame = Frame(self.root)
        button_frame.pack(pady=10)

        self.add_button = Button(button_frame, text="Ajouter un livre", font=('Verdana', 12, 'bold'), command=self.add_book)
        self.add_button.pack(side=LEFT, padx=10)

        self.edit_button = Button(button_frame, text="Modifier un livre", font=('Verdana', 12, 'bold'), command=self.edit_book)
        self.edit_button.pack(side=LEFT, padx=10)

        self.remove_button = Button(button_frame, text="Supprimer un livre", font=('Verdana', 12, 'bold'), command=self.remove_book)
        self.remove_button.pack(side=LEFT, padx=10)

        self.update_treeview()

    def research_book_by_title(self) :
        search_title = self.research_entry_title.get().strip().lower()
        filtered_books = [b for b in self.book_manager.books if search_title in b.title.lower()]
        if not filtered_books :
            messagebox.showwarning("Aucun livre de ce titre n'a été trouvé !")
        self.update_treeview(filtered_books)

    def research_book_by_isbn(self) :
        search_isbn = self.research_entry_isbn.get().strip().lower()
        filtered_books = [b for b in self.book_manager.books if search_isbn in str(b.isbn).lower()]
        if not filtered_books :
            messagebox.showwarning("Aucun livre avec ce numéro n'a été trouvé !")
        self.update_treeview(filtered_books)

    def research_book_by_authors(self) :
        search_authors = self.research_entry_authors.get().strip().lower()
        filtered_books = [b for b in self.book_manager.books if any(search_authors in author.lower() for author in b.authors)]
        if not filtered_books :
            messagebox.showwarning("Aucun livre avec cet/ces auteur(s) n'a été trouvé !")
        self.update_treeview(filtered_books)

    def update_treeview(self, books=None) :
        self.tree.delete(*self.tree.get_children())
        books = books or self.book_manager.books
        for book in books :
            self.tree.insert('', 'end', values=(
                book.book_id,
                book.title,
                 ', '.join(book.authors),
                book.publication_year,
                book.isbn,
                 ', '.join(book.editors),
                ', '.join(book.collections),
                ', '.join(book.genres),
                'Disponible' if book.is_available else 'Indisponible'
                ))
    
    def refresh_list(self) :
        self.update_treeview()

    def edit_book(self) :
        selected_item = self.tree.selection()
        if not selected_item :
            messagebox.showwarning("Veuillez entrer un livre à modifier.")
            return
        
        selected_book_id = self.tree.item(selected_item[0])['values'][0]
        book = next((b for b in self.book_manager.books if b.book_id == selected_book_id), None)

        self.add_book(book)

    def remove_book(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Veuillez entrer un livre à supprimer.")
            return

        selected_book_id = self.tree.item(selected_item[0])['values'][0]
        self.book_manager.remove_book(selected_book_id)
        self.update_treeview()
        

    def add_book(self, book=None):
        self.form_wind = Toplevel(self.root)
        self.form_wind.title("Formulaire Livre")

        wind_width = 700
        wind_height = 350

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        position_x = (screen_width // 2) - (wind_width // 2)
        position_y = (screen_height // 2) - (wind_height // 2)

        self.form_wind.geometry(f"{wind_width}x{wind_height}+{position_x}+{position_y}")

        book_id = book.book_id if book else Book.book_number

        self.book_id_label = Label(self.form_wind, text="N° : ")
        self.book_id_label.grid(row=0, column=0, sticky='E')
        self.book_id_entry = Entry(self.form_wind, state="readonly", textvariable=StringVar(self.form_wind, value=str(book_id)))
        self.book_id_entry.grid(row=0, column=1)

        validate_cmd = (self.form_wind.register(self.validate_title), '%P')

        self.title_label = Label(self.form_wind, text="Titre : ")
        self.title_label.grid(row=1, column=0, sticky='E')
        self.title_entry = Entry(self.form_wind, validate="key", validatecommand=validate_cmd)
        self.title_entry.grid(row=1, column=1)
        self.title_entry.insert(0, book.title if book else " ")
        self.title_entry.focus_set()

        self.authors_label = Label(self.form_wind, text="Auteurs : ")
        self.authors_label.grid(row= 2, column=0, sticky='E')
        self.authors_entry = Entry(self.form_wind)
        self.authors_entry.grid(row=2, column=1)
        self.authors_entry.insert(0, ", ".join(book.authors) if book else " ")

        validate_year_cmd = (self.form_wind.register(self.validate_year), '%P') 
        
        self.publi_year_label = Label(self.form_wind, text="Année de publication : ")
        self.publi_year_label.grid(row=3, column=0, sticky='E')
        self.publi_year_entry = Entry(self.form_wind, validate="key", validatecommand=validate_year_cmd)
        self.publi_year_entry.grid(row=3, column=1)
        self.publi_year_entry.insert(0, str(book.publication_year) if book else " ")

        validate_num_cmd = (self.form_wind.register(self.validate_number), '%P')

        self.numb_label = Label(self.form_wind, text="ISBN : ")
        self.numb_label.grid(row=4, column=0, sticky='E')
        self.numb_entry = Entry(self.form_wind, validate="key", validatecommand=validate_num_cmd)
        self.numb_entry.grid(row=4, column=1)
        self.numb_entry.insert(0, book.isbn if book else " ")

        self.editors_label = Label(self.form_wind, text="Editeur(s) : ")
        self.editors_label.grid(row=5, column=0, sticky='E')
        self.editors_list = Listbox(self.form_wind, selectmode=MULTIPLE)
        self.editors_list.grid(row=5, column=1)
        for editor in self.book_manager.editors :
            self.editors_list.insert(END, editor)
        if book :
            for editor in book.editors :
                i = self.book_manager.editors.index(editor)
                self.editors_list.select_set(i)

        self.coll_label = Label(self.form_wind, text="Collection(s) : ")
        self.coll_label.grid(row=6, column=0, sticky='E')
        self.coll_list= Listbox(self.form_wind, selectmode=MULTIPLE)
        self.coll_list.grid(row=6, column=1)
        for coll in self.book_manager.collections :
            self.coll_list.insert(END, coll)
        if book :
            for coll in book.collections :
                i = self.book_manager.collections.index(coll)
                self.coll_list.select_set(i)

        self.genre_label = Label(self.form_wind, text="Genre(s) : ")
        self.genre_label.grid(row=7, column=0, sticky='E')
        self.genre_list = Listbox(self.form_wind, selectmode=MULTIPLE)
        self.genre_list.grid(row=7, column=1)
        for genre in self.book_manager.genres:
            self.genre_list.insert(END, genre)
        if book:
            for genre in book.genres :
                i = self.book_manager.genres.index(genre)
                self.genre_list.select_set(i)

        self.available_label = Label(self.form_wind, text="Disponibilité : ")
        self.available_label.grid(row=8, column=0, sticky='E')
        self.available_var = BooleanVar(value=book.is_available if book else True)
        self.available_check = Checkbutton(self.form_wind, variable=self.available_var)
        self.available_check.grid(row=8, column=1)

        self.submit_button = Button(self.form_wind, text="Valider", command=lambda: self.save_book(book))
        self.submit_button.grid(row=9, column=0, columnspan=2)

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
        editors = [self.editors_list.get(i) for i in self.editors_list.curselection()]
        collections = [self.coll_list.get(i) for i in self.coll_list.curselection()]
        genres = [self.genre_list.get(i) for i in self.genre_list.curselection()]
        is_available = self.available_var.get()

        if not all([title, authors, publication_year, isbn, editors, collections, genres]):
            messagebox.showwarning("Veuillez remplir tous les champs !")
            return
        
        new_book = Book(book_id, title, authors, publication_year, isbn, editors, collections, genres, is_available)

        if book:
            self.book_manager.update_book(new_book)
        else:
            self.book_manager.add_book(new_book)

        self.update_treeview()
        self.form_wind.destroy()