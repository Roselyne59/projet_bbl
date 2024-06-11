import tkinter as tk
from borrow import Borrow
from borrowManager import BorrowManager

class BorrowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestion des Emprunts")
        self.borrow_manager = BorrowManager()

        self.listbox = tk.Listbox(self.root, width=150, height=20)
        self.listbox.pack(pady=10)

        self.load_borrows()

    def load_borrows(self):
        self.listbox.delete(0, tk.END)
        for borrow in self.borrow_manager.borrows:
            self.listbox.insert(tk.END, f"ID Emprunt: {borrow.borrow_id}")
            borrow_info = [
                f"ID Utilisateur: {borrow.user_id}",
                f"ID Livre: {borrow.book_id}",
                f"Date de début: {borrow.start_date}",
                f"Date de fin: {borrow.due_date}",
                f"Approuvé: {'Oui' if borrow.is_approved else 'Non'}"
            ]
            for item in borrow_info:
                self.listbox.insert(tk.END, item)
            self.listbox.insert(tk.END, "------------------------------")

root = tk.Tk()
app = BorrowApp(root)
root.mainloop()
