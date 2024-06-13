import json
from reservation import Reservation

class ReservationManager:
    def __init__(self, filepath='json/reservations.json'):
        self.filepath = filepath
        self.reservations = self.load_reservations()

    def load_reservations(self):
        try:
            with open(self.filepath, 'r') as file:
                data = json.load(file)
                return [Reservation.from_dict(item) for item in data]
        except FileNotFoundError:
            return []

    def save_reservations(self):
        with open(self.filepath, 'w') as file:
            json.dump([res.to_dict() for res in self.reservations], file, indent=4)
        print("Réservations enregistrées dans le fichier JSON.")

    def add_reservation(self, reservation):
        self.reservations.append(reservation)
        self.save_reservations()

    def get_all_reservations(self):
        return self.reservations

    def remove_reservation(self, reservation):
        self.reservations = [res for res in self.reservations if not (res.user_id == reservation.user_id and res.book_id == reservation.book_id and res.start_date == reservation.start_date and res.end_date == reservation.end_date)]
        self.save_reservations()
        print(f"Réservation supprimée: {reservation.to_dict()}")

    def update_reservation(self, reservation):
        for i, res in enumerate(self.reservations):
            if res.user_id == reservation.user_id and res.book_id == reservation.book_id and res.start_date == reservation.start_date and res.end_date == reservation.end_date:
                self.reservations[i] = reservation
                self.save_reservations()
                print(f"Réservation mise à jour: {reservation.to_dict()}")
                return
