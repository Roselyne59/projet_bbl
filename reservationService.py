# Importation des modules nécessaires
import os
import json
from reservation import Reservation

# Définition de la classe ReservationService pour gérer les opérations liées aux réservations
class ReservationService:
    def __init__(self, json_file="reservations.json"):
        self.json_file = json_file
        self.reservations = self.load_reservations()

    # Méthode pour charger les réservations depuis le fichier JSON
    def load_reservations(self):
        if not os.path.exists(self.json_file):
            return []
        try:
            with open(self.json_file, 'r') as file:
                reservations_data = json.load(file)
                return [Reservation(**reservation_data) for reservation_data in reservations_data]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Erreur de chargement des réservations: {e}")
            return []

    # Méthode pour sauvegarder les réservations dans le fichier JSON
    def save_reservations(self):
        try:
            with open(self.json_file, 'w') as file:
                json.dump([reservation.__dict__ for reservation in self.reservations], file, indent=4)
        except IOError as e:
            print(f"Erreur de sauvegarde des réservations: {e}")

    # Méthode pour ajouter une réservation
    def add_reservation(self, reservation):
        self.reservations.append(reservation)
        self.save_reservations()

    # Méthode pour supprimer une réservation
    def remove_reservation(self, reservation):
        self.reservations.remove(reservation)
        self.save_reservations()

# Test de la classe ReservationService
if __name__ == "__main__":
    # Exemple d'utilisation de la classe ReservationService
    reservation_service = ReservationService()
    reservation = Reservation(book_id=1, user_id=2)
    reservation_service.add_reservation(reservation)
    print("Réservations chargées:", reservation_service.reservations)


        