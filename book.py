
class Book:
    def __init__(self, title, authors, publication_year, isbn, editor, genders, id=None):
        self.id = id
        self.title = title
        self.authors = authors
        self.publication_year = publication_year
        self.isbn = isbn
        self.editor = editor
        self.genders = genders

    def __str__(self):
        return f"{self.title} by {', '.join(self.authors)} ({self.publication_year})"

    def resume(self):
        return f"{self.title} - {self.editor} - {', '.join(self.genders)}"


