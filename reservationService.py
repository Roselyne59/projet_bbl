import json 
import os 
from reservation import Reservation 

class resrvationService:
    def __init__(self, json_file = "reservations.json"):
        self.json_file = json_file
        self.reservations = []
        self.load.reservations()