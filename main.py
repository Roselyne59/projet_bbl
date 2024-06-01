import tkinter as tk
from login import Login
from userService import UserService
from bookService import BookService

if __name__ == "__main__":
    root = tk.Tk()

    userService = UserService()
    bookService = BookService()

    login_app = Login(root, userService, bookService)

    root.mainloop()

