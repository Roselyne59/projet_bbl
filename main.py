import json
from user import User
from book import Book
from userApp import UserApp
from bookApp import BookApp
from userManager import UserManager
from bookManager import BookManager
import tkinter as tk


if __name__ == "__main__":
    root_user = tk.Tk()
    root_book = tk.Tk()

    user_manager = UserManager()
    book_manager = BookManager()
    user_app = UserApp(root_user)
    book_app = BookApp(root_book)

    root_user.mainloop()
    root_book.mainloop()