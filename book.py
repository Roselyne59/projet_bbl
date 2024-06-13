
class Book:
    book_number = 1

    def __init__(self, book_id,title, authors, publication_year, isbn, editor, collections, genres, is_available = True):
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.publication_year = publication_year
        self.isbn = isbn
        self.editor = editor
        self.collections = collections
        self.genres = genres
        self.is_available = is_available
        if book_id >= Book.book_number:
            Book.book_number = book_id + 1

    def __str__(self):
        return f"{self.title} by {', '.join(self.authors)} ({self.publication_year})"

    def resume(self):
        return f"{self.title} - {self.editor} - {', '.join(self.genres)}"
    
    def to_dict (self):
        return{
            "book_id" : self.book_id,
            "titre" : self.title,
            "auteurs" : self.authors,
            "année de publication" : self.publication_year,
            "isbn" : self.isbn,
            "éditeur" : self.editor,
            "collection" : self.collections,
            "genres" : self.genres,
            "is_available" : self.is_available
        }

    @staticmethod
    def from_dict (data) :
        return Book(
            data["book_id"],
            data["titre"],
            data["auteurs"],
            data["année de publication"],
            data["isbn"],
            data["éditeur"],
            data["collection"],
            data["genres"],
            data["is_available"]
        )
