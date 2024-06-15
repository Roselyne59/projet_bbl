import tkinter as tk
from models.login import LoginApp



if __name__ == "__main__":
    """
        Main entry point for the application.

        This script initializes the Tkinter root window and starts the LoginApp.
    """
    root = tk.Tk()
    app = LoginApp(root)
    root.mainloop()