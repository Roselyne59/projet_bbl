import json
from models.reservation import Reservation

class ReservationManager:
    """
    Class to manage book reservations.

    Attributes:
        filepath (str): The path to the JSON file where reservations are stored.
        reservations (list): A list of Reservation objects.
    """
    def __init__(self, filepath='json/reservations.json'):
        """
        Initializes the ReservationManager with the given filepath.

        Args:
            filepath (str, optional): The path to the JSON file. Defaults to 'json/reservations.json'.
        """
        self.filepath = filepath
        self.reservations = self.load_reservations()

    def load_reservations(self):
        """
        Loads reservations from the JSON file.

        Returns:
            list: A list of Reservation objects.
        """
        try:
            with open(self.filepath, 'r') as file:
                data = json.load(file)
                return [Reservation.from_dict(item) for item in data]
        except FileNotFoundError:
            return []

    def save_reservations(self):
        """
        Saves the current reservations to the JSON file.
        """
        with open(self.filepath, 'w') as file:
            json.dump([res.to_dict() for res in self.reservations], file, indent=4)
        print("Réservations enregistrées dans le fichier JSON.")

    def add_reservation(self, reservation):
        """
        Adds a new reservation and saves the updated list to the JSON file.

        Args:
            reservation (Reservation): The reservation to add.
        """
        self.reservations.append(reservation)
        self.save_reservations()

    def get_all_reservations(self):
        """
        Retrieves all reservations.

        Returns:
            list: A list of all Reservation objects.
        """
        return self.reservations

    def remove_reservation(self, reservation):
        """
        Removes a reservation and saves the updated list to the JSON file.

        Args:
            reservation (Reservation): The reservation to remove.
        """
        self.reservations = [res for res in self.reservations if not (res.user_id == reservation.user_id and res.book_id == reservation.book_id and res.start_date == reservation.start_date and res.end_date == reservation.end_date)]
        self.save_reservations()
        print(f"Réservation supprimée: {reservation.to_dict()}")

    def update_reservation(self, reservation):
        """
        Updates an existing reservation and saves the updated list to the JSON file.

        Args:
            reservation (Reservation): The reservation to update.
        """
        for i, res in enumerate(self.reservations):
            if res.user_id == reservation.user_id and res.book_id == reservation.book_id and res.start_date == reservation.start_date and res.end_date == reservation.end_date:
                self.reservations[i] = reservation
                self.save_reservations()
                print(f"Réservation mise à jour: {reservation.to_dict()}")
                return
