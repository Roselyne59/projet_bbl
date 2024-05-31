import json
import os
from reservation import Reservation


#  Initialise le service de réservation avec un fichier JSON.
#  Charge les réservations depuis le fichier JSON si celui-ci existe.

class ReservationService:
    def __init__(self, json_file="reservations.json"):
        self.json_file = json_file
        self.reservations = []
        self.load_reservations()

    # Charge les réservations depuis le fichier JSON.
    # Si le fichier n'existe pas, la liste des réservations reste vide.
    def load_reservations(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as file:
                reservations_data = json.load(file)
                for data in reservations_data:
                    reservation = Reservation(
                        user=data.get("user"),
                        book=data.get("book"),
                        reservation_date=data.get("reservation_date")
                    )
                    if "cancelled" in data:
                        reservation.cancelled = data.get("cancelled")
                    self.reservations.append(reservation)

    # Sauvegarde les réservations actuelles dans le fichier JSON.
    # Écrit toutes les réservations de la liste dans le fichier.
    def save_reservations(self):
        reservations_data = []
        for reservation in self.reservations:
            reservation_data = {
                "user": reservation.user,
                "book": reservation.book,
                "reservation_date": reservation.reservation_date,
                "cancelled": reservation.cancelled
            }
            reservations_data.append(reservation_data)

        with open(self.json_file, 'w') as file:
            json.dump(reservations_data, file, indent=4)

    # Ajoute une nouvelle réservation à la liste et la sauvegarde dans le fichier JSON.
    def add_reservation(self, user, book, reservation_date):
        reservation = Reservation(user, book, reservation_date)
        self.reservations.append(reservation)
        self.save_reservations()

    # Supprime une réservation de la liste et met à jour le fichier JSON.
    def delete_reservation(self, reservation):
        self.reservations.remove(reservation)
        self.save_reservations()

        