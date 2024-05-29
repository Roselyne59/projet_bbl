import tkinter as tk
from tkinter import messagebox, simpledialog
from bookService import BookService
from book import Book

class Library:
    def __init__(self, root) :
        self.root = root
        self.root.title("Library Application")

        self.book_service = BookService()

        self.create_widgets()
        self.update_list()
#Créer une liste de genre
#Vérifier collection
    
    def create_widgets(self):
        self.list = tk.Listbox(self.root, width=114, height=10)
        self.list.pack(pady=10)

        self.add_book_button = tk.Button(self.root, text="Add a book", command=self.add_book)
        self.add_book_button.pack(pady=10)

        self.delete_book_button = tk.Button(self.root, text="Delete a book", command=self.delete_book)
        self.delete_book_button.pack(pady=10)

        self.search_book_button = tk.Button(self.root, text="Research", command=self.search_book)
        self.search_book_button.pack(pady=10)

        self.list_books_button = tk.Button(self.root, text="List of books", command=self.book_list)
        self.list_books_button.pack(pady=10)

#        self.add_shelf_button = tk.Button(self.root, text="Add a shelf", command=self.add_shelf)
#        self.add_shelf_button.pack(pady=10)

    def add_book(self):
        title = None
        while not title:
            title = simpledialog.askstring("Title", "Enter the title:")
            if not title:
                messagebox.showerror("Input Error", "Please fill in the title.")

        authors = None
        while not authors:
            authors_input = simpledialog.askstring("Authors", "Enter the authors (comma-separated):")
            if authors_input:
                authors = authors_input.split(",")
            else:
                messagebox.showerror("Input Error", "Please fill in the authors.")

        isbn = None
        while not isbn:
            isbn = simpledialog.askstring("ISBN", "Enter the ISBN:")
            if not isbn:
                messagebox.showerror("Input Error", "Please fill in the ISBN.")

        editor = None
        while not editor:
            editor = simpledialog.askstring("Editor", "Enter the editor:")
            if not editor:
                messagebox.showerror("Input Error", "Please fill in the editor.")

        publication_year = None
        while not publication_year:
            publication_year = simpledialog.askstring("Year of Publication", "Enter the year of publication:")
            if not publication_year:
                messagebox.showerror("Input Error", "Please fill in the year of publication.")

        genders = None
        while not genders:
            genders_input = simpledialog.askstring("Genres", "Enter the genres (comma-separated):")
            if genders_input:
                genders = genders_input.split(",")
            else:
                messagebox.showerror("Input Error", "Please fill in the genres.")

        book = Book(
            title=title,
            authors=authors,
            isbn=isbn,
            editor=editor,
            publication_year=int(publication_year),
            genders=genders
        )
        self.book_service.add_book(book)
        self.update_list()


    def delete_book(self):
        title = simpledialog.askstring("Title", "Enter the title of the book to delete:")
        if not title:
            return
        book = next((b for b in self.book_service.books if b.title == title), None)
        if book is None:
            messagebox.showerror("Error", "Book not found!")
            return
        
        self.book_service.remove_book(book)
        self.update_list()

    def search_book(self, title):
        pass

    def book_list(self):
        self.update_list()

    def add_shelf(self):
        pass

    def login(self):
        pass

    def user_list(self):
        #Only for admin
        pass


    def update_list(self):
        self.list.delete(0,tk.END)
        for book in self.book_service.books:
            self.list.insert(tk.END, f"{book.title} by {','.join(book.authors)}")