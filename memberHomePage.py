from userHomePage import UserHomePage
from bookApp import BookApp

class MemberHomePage(UserHomePage):
    def __init__(self, root, nom, prenom):
        super().__init__(root, nom, prenom)
        self.root = root
        self.clear_screen()
        self.root.title("Espace Membre")

        self.welcome_message(nom, prenom)
        self.logout_bouton()

        self.book_app = BookApp(root)
        self.__show_book_list()
    
    def __show_book_list(self):
         self.book_app.update_list()
    

