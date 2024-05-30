import tkinter as tk
from tkinter import messagebox, simpledialog
from bookService import BookService
from book import Book
from userService import UserService
from user import User

class Library:
    def __init__(self, root) :
        self.root = root
        self.root.title("Library Application")

        self.book_service = BookService()
        self.user_service = UserService()

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

        self.user_add_button = tk.Button(self.root, text="Add a user", command=self.user_add)
        self.user_add_button.pack(pady=10)

        self.user_list_button = tk.Button(self.root, text="List of users", command=self.user_list_show)
        self.user_list_button.pack(pady=10)

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


    def user_add(self):
        firstname = None 
        while not firstname:
            firstname = simpledialog.askstring("Firstname", "Enter your firstname : ")
            if not firstname:
                messagebox.showerror("Error ! ", "Please fill in the firstname !")
        
        lastname = None
        while not lastname:
            lastname = simpledialog.askstring("Last Name", "Enter the last name:")
            if not lastname:
                messagebox.showerror("Input Error", "Please fill in the last name.")

        birthdate = None
        while not birthdate:
            birthdate = simpledialog.askstring("Birthdate", "Enter the birthdate (YYYY-MM-DD):")
            if not birthdate:
                messagebox.showerror("Input Error", "Please fill in the birthdate.")

        email = None
        while not email:
            email = simpledialog.askstring("Email", "Enter the email address:")
            if not email:
                messagebox.showerror("Input Error", "Please fill in the email address.")

        address = None
        while not address:
            address = simpledialog.askstring("Address", "Enter the address:")
            if not address:
                messagebox.showerror("Input Error", "Please fill in the address.")
        
        is_admin = messagebox.askyesno("Admin", "Are you an admin ?")

        user = User(
            firstname=firstname,
            lastname=lastname,
            birthdate=birthdate,
            email=email,
            address=address,
            is_admin=is_admin
        )
        self.user_service.add_user(user)


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

    def search_book(self):
        title = simpledialog.askstring("Title", "Enter the title of the book to search:")
        if not title:
            return
        
        book = next((b for b in self.book_service.books if b.title == title), None)
        if book is None:
            messagebox.showinfo("Book not found !")
        else:
            messagebox.showinfo("Result : ", f"Found the book: {book.title} by {', ' .join(book.authors)}")

    def book_list(self):
        self.update_list()

 #   def add_shelf(self):
 #       pass

    def update_list(self):
        self.list.delete(0,tk.END)
        for book in self.book_service.books:
            self.list.insert(tk.END, f"{book.title} by {','.join(book.authors)}")

    
    
    def user_list_show(self):
        user_list_window = tk.Toplevel(self.root)
        user_list_window.title("List of users.")

        list_users = tk.Listbox(user_list_window, width=100, height=10)
        list_users.pack(pady=10)

        for user in self.user_service.get_users():
            list_users.insert(tk.END, str(user))

    #search user by name
    def user_search(self, name): 
        results = self.user_service.search_user(name)
        return results