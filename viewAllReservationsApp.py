import tkinter as tk
from tkinter import ttk, messagebox
from reservationManager import ReservationManager
from reservation import Reservation
from bookManager import BookManager
from userManager import UserManager

class ViewAllReservationsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Toutes les réservations")

        self.reservation_manager = ReservationManager()
        self.book_manager = BookManager()
        self.user_manager = UserManager()

        self.reservation_dict = {}

        self.tree = ttk.Treeview(root, columns=("user_id", "user_name", "user_email", "book_id", "book_title", "start_date", "end_date", "status"), show='headings')
        self.tree.heading("user_id", text="ID Utilisateur")
        self.tree.heading("user_name", text="Nom Utilisateur")
        self.tree.heading("user_email", text="Email Utilisateur")
        self.tree.heading("book_id", text="ID Livre")
        self.tree.heading("book_title", text="Titre Livre")
        self.tree.heading("start_date", text="Date Début")
        self.tree.heading("end_date", text="Date Fin")
        self.tree.heading("status", text="Statut")

        self.tree.pack(fill=tk.BOTH, expand=True)

        self.populate_tree()

        self.accept_button = tk.Button(root, text="Accepter", command=self.accept_reservation)
        self.accept_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.reject_button = tk.Button(root, text="Refuser", command=self.reject_reservation)
        self.reject_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Supprimer", command=self.delete_reservation)
        self.delete_button.pack(side=tk.LEFT, padx=10, pady=10)

    def populate_tree(self):
        self.tree.delete(*self.tree.get_children())
        for reservation in self.reservation_manager.get_all_reservations():
            user = self.user_manager.get_user_by_id(reservation.user_id)
            book_title = self.book_manager.get_book_title_by_id(reservation.book_id)
            user_name = f"{user.lastname} {user.firstname}"
            status = getattr(reservation, "status", "attente")
            item_id = self.tree.insert("", "end", values=(reservation.user_id, user_name, user.email, reservation.book_id, book_title, reservation.start_date, reservation.end_date, status))
            self.reservation_dict[item_id] = reservation

    def accept_reservation(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Erreur", "Veuillez sélectionner une réservation.")
            return
        for item in selected_item:
            reservation = self.reservation_dict.get(item)
            if reservation:
                user = self.user_manager.get_user_by_id(reservation.user_id)
                book_title = self.book_manager.get_book_title_by_id(reservation.book_id)
                reservation.status = "Acceptée"
                self.update_reservation(reservation)
                self.tree.item(item, values=(reservation.user_id, f"{user.lastname} {user.firstname}", user.email, reservation.book_id, book_title, reservation.start_date, reservation.end_date, "Acceptée"))
                print(f"Réservation acceptée: {reservation.to_dict()}")

    def reject_reservation(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Erreur", "Veuillez sélectionner une réservation.")
            return
        for item in selected_item:
            reservation = self.reservation_dict.get(item)
            if reservation:
                user = self.user_manager.get_user_by_id(reservation.user_id)
                book_title = self.book_manager.get_book_title_by_id(reservation.book_id)
                reservation.status = "Refusée"
                self.update_reservation(reservation)
                self.tree.item(item, values=(reservation.user_id, f"{user.lastname} {user.firstname}", user.email, reservation.book_id, book_title, reservation.start_date, reservation.end_date, "Refusée"))
                print(f"Réservation refusée: {reservation.to_dict()}")

    def delete_reservation(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showerror("Erreur", "Veuillez sélectionner une réservation.")
            return
        for item in selected_item:
            reservation = self.reservation_dict.pop(item, None)
            if reservation:
                self.reservation_manager.remove_reservation(reservation)
                self.tree.delete(item)
                print(f"Réservation supprimée: {reservation.to_dict()}")
        self.reservation_manager.save_reservations()
        self.populate_tree()

    def update_reservation(self, reservation):
        self.reservation_manager.update_reservation(reservation)
        print(f"Réservation mise à jour dans le gestionnaire: {reservation.to_dict()}")

