import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from bookService import BookService
from userService import UserService
from book import Book

class Library:
    def __init__(self, root, book_service, user_service, current_user):
        self.root = root
        self.book_service = book_service
        self.user_service = user_service
        self.current_user = current_user
        self.root.title("Library Application")
        self.setup_widgets()
        self.refresh_book_list()

    def setup_widgets(self):
        self.frame = ttk.Frame(self.root, padding="250 250 250 250")
        self.frame.pack(fill=tk.BOTH, expand=True)

        self.list = tk.Listbox(self.frame, width=50, height=20)
        self.list.grid(row=0, column=0, columnspan=4, pady=10)

        button_width = 8

        self.add_book_button = tk.Button(self.frame, text="Add Book", command=self.show_add_book_form, width=button_width)
        self.add_book_button.grid(row=1, column=0, pady=5, padx=5)

        tk.Button(self.frame, text="Show Users", command=self.show_users, width=button_width).grid(row=1, column=1, pady=5, padx=5)
        tk.Button(self.frame, text="Show Books", command=self.refresh_book_list, width=button_width).grid(row=1, column=2, pady=5, padx=5)
        tk.Button(self.frame, text="Delete Book", command=self.delete_book, width=button_width).grid(row=1, column=3, pady=5, padx=5)

    def show_add_book_form(self):
        self.add_book_button.config(state=tk.DISABLED)

        labels = ['Title', 'Authors (comma-separated)', 'Publication Year', 'ISBN', 'Editor', 'Genres (comma-separated)']
        self.entries = {}
        self.form_widgets = []

        for idx, label in enumerate(labels):
            lbl = tk.Label(self.frame, text=label)
            lbl.grid(row=5 + idx, column=0, pady=5, padx=5, sticky=tk.W)
            entry = tk.Entry(self.frame, width=30)
            entry.grid(row=5 + idx, column=1, pady=5, padx=5)
            self.entries[label] = entry
            self.form_widgets.append(lbl)
            self.form_widgets.append(entry)

        self.submit_button = tk.Button(self.frame, text="Submit", command=self.submit_book)
        self.submit_button.grid(row=5 + len(labels), column=0, columnspan=2, pady=10)
        self.form_widgets.append(self.submit_button)

    def submit_book(self):
        book_info = {label: entry.get() for label, entry in self.entries.items()}
        if any(not info for info in book_info.values()):
            messagebox.showerror("Error", "All fields must be filled out.")
            return
        book = Book(
            title=book_info['Title'],
            authors=book_info['Authors (comma-separated)'].split(','),
            publication_year=int(book_info['Publication Year']),
            isbn=book_info['ISBN'],
            editor=book_info['Editor'],
            genders=book_info['Genres (comma-separated)'].split(',')
        )
        self.book_service.add_book(book)
        self.refresh_book_list()
        self.clear_form()

    def clear_form(self):
        for widget in self.form_widgets:
            widget.destroy()
        self.add_book_button.config(state=tk.NORMAL)
        self.form_widgets.clear()

    def delete_book(self):
        title = simpledialog.askstring("Delete Book", "Enter the title of the book to delete:")
        book = self.book_service.find_book_by_title(title)
        if book:
            self.book_service.remove_book(book)
            self.refresh_book_list()
        else:
            messagebox.showerror("Error", "Book not found!")

    def refresh_book_list(self):
        self.list.delete(0, tk.END)
        for book in self.book_service.books:
            self.list.insert(tk.END, str(book))

    def show_users(self):
        user_list_window = tk.Toplevel(self.root)
        user_list_window.title("List of Users")
        list_users = tk.Listbox(user_list_window, width=50, height=10)
        list_users.pack(pady=20, padx=20)

        for user in self.user_service.get_users():
            list_users.insert(tk.END, str(user))






