
import json
from user import User
from userApp import UserApp
from userManager import UserManager
import tkinter as tk


if __name__ == "__main__":
    root = tk.Tk()
    app = UserApp(root)
    user_manager = UserManager() 
    root.mainloop()