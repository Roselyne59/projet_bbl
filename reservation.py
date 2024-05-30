from user import User
from book import Book 

class Reservation:
    def __init__(self, user, book, reservation_date):
        self.user = user
        self.book = book
        self.reservation_date = reservation_date
        self.cancelled = False
        
    #METHODE POUR ANNULER LA RESERVATION
    def cancel(self):
        
        #Vérifie si la réservation a déjà été annulée 
        if not self.cancelled:
            self.canceled = True
            print(f"Reservation for {self.book.title} has been cancelled.")
        else:
            print("Reservation has already been cancelled.")