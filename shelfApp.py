class Shelf :
    shelf_number = 1
    
    def __init__(self, shelf_id, number, letter) :
        self.shelf_id = shelf_id
        self.number = number
        self.letter = letter
        if shelf_id >= Shelf.shelf_number :
            Shelf.shelf_number = shelf_id + 1

    def __str__(self) :
        return f"{self.number}{self.letter}"
    
    def to_dict(self) :
        return{
            "shelf_id" : self.shelf_id,
            "number" : self.number,
            "letter" : self.letter
        }
    
    @staticmethod
    def from_dict(data) :
        return Shelf(
            data["shelf_id"],
            data["number"],
            data["letter"]
        )
    