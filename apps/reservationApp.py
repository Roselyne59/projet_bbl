import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
from managers.reservationManager import ReservationManager
from models.reservation import Reservation
from managers.bookManager import BookManager
from datetime import date


class ReservationApp:
    def __init__(self, root, user_id):
        self.root = root
        self.root.title("Application de Réservation")
        self.user_id = user_id

        self.reservation_manager = ReservationManager()
        self.book_manager = BookManager()

        self.book_list = [book.title for book in self.book_manager.books]

        self.user_id_label = tk.Label(root, text="ID Utilisateur")
        self.user_id_label.grid(row=0, column=0)
        self.user_id_value = tk.Label(root, text=self.user_id)
        self.user_id_value.grid(row=0, column=1)

        self.book_label = tk.Label(root, text="Sélectionnez un Livre")
        self.book_label.grid(row=1, column=0)
        self.book_combobox = ttk.Combobox(root, values=self.book_list)
        self.book_combobox.grid(row=1, column=1)

        self.start_date_label = tk.Label(root, text="Date de Début")
        self.start_date_label.grid(row=2, column=0)
        self.start_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.start_date_entry.grid(row=2, column=1)

        self.end_date_label = tk.Label(root, text="Date de Fin")
        self.end_date_label.grid(row=3, column=0)
        self.end_date_entry = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.end_date_entry.grid(row=3, column=1)

        self.submit_button = tk.Button(root, text="Soumettre la Réservation", command=self.submit_reservation)
        self.submit_button.grid(row=4, column=0, columnspan=2)

        self.reservation_tree = ttk.Treeview(root,
                                             columns=("book_id", "book_title", "start_date", "end_date", "status"),
                                             show="headings")
        self.reservation_tree.heading("book_id", text="ID Livre")
        self.reservation_tree.heading("book_title", text="Titre du Livre")
        self.reservation_tree.heading("start_date", text="Date de Début")
        self.reservation_tree.heading("end_date", text="Date de Fin")
        self.reservation_tree.heading("status", text="Statut")
        self.reservation_tree.grid(row=5, column=0, columnspan=2, pady=20)

        self.view_reservations()

    def submit_reservation(self):
        book_title = self.book_combobox.get()
        book_id = self.book_manager.get_book_id_by_title(book_title)
        start_date = self.start_date_entry.get_date()
        end_date = self.end_date_entry.get_date()
        today = date.today()

        if start_date < today:
            messagebox.showerror("Erreur", "La date de début ne peut pas être dans le passé.")
            return

        if end_date < today:
            messagebox.showerror("Erreur", "La date de fin ne peut pas être dans le passé.")
            return

        if end_date < start_date:
            messagebox.showerror("Erreur", "La date de fin ne peut pas être antérieure à la date de début.")
            return

        existing_reservations = self.reservation_manager.get_all_reservations()
        for res in existing_reservations:
            if res.user_id == self.user_id and res.book_id == book_id:
                messagebox.showerror("Erreur", "Vous avez déjà réservé ce livre.")
                return

        reservation = Reservation(self.user_id, book_id, start_date, end_date)
        self.reservation_manager.add_reservation(reservation)
        messagebox.showinfo("Succès", "Réservation soumise avec succès.")
        self.view_reservations()

    def view_reservations(self):
        for row in self.reservation_tree.get_children():
            self.reservation_tree.delete(row)

        reservations = self.reservation_manager.get_all_reservations()
        user_reservations = [res for res in reservations if res.user_id == self.user_id]

        if not user_reservations:
            return

        for res in user_reservations:
            book_title = self.book_manager.get_book_title_by_id(res.book_id)
            status = getattr(res, "status", "En attente")
            self.reservation_tree.insert("", "end",
                                         values=(res.book_id, book_title, res.start_date, res.end_date, status))


