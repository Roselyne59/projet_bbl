import tkinter as tk

class MemberHomePage:
    def __init__(self, root):
        self.root = root
        self.clear_screen()
        self.root.title("Espace Membre")

        # Add the rest of your user interface code here
        # For example, you can call self.main_interface() if it is the same as user interface

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()