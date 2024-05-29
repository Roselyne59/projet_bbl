import uuid

class Book:
    def __init__(self, title, authors, publication_year, isbn, editor, genders):
        self.id = str(uuid.uuid4())
        self.title = title
        self.authors = authors
        self.publication_year = publication_year
        self.isbn = isbn
        self.editor = editor
        self.genders = genders
    

    #creer une liste des genres 

    def resume(self):
        pass

    def book_request(self):
        pass

    def reserve_status(self):
        pass