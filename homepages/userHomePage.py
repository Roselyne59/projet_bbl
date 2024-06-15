import tkinter as tk

class UserHomePage:
    """
    Base class for user home pages.

    Attributes:
        root (tk.Tk): The root window of the Tkinter application.
    """
    def __init__(self, root, firstname, lastname):
        """
        Initializes the UserHomePage with the given root window, first name, and last name.

        Args:
            root (tk.Tk): The root window of the Tkinter application.
            firstname (str): The first name of the user.
            lastname (str): The last name of the user.
        """
        self.root = root
        self.clear_screen()
        
        self.welcome_message(firstname, lastname)
        self.logout_bouton()

    def clear_screen(self):
        """
        Clears the current screen by destroying all widgets in the root window.
        """
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def welcome_message(self, firstname, lastname):
        """
        Displays a welcome message with the user's first and last name.

        Args:
            firstname (str): The first name of the user.
            lastname (str): The last name of the user.
        """
        welcome_message= f"Bienvenue {firstname} {lastname}"
        welcome_label = tk.Label(self.root, text = welcome_message, font=('helvetica', 16, 'bold'), fg='red')
        welcome_label.pack(pady=20)
    
    def logout_bouton(self):
        """
        Displays a logout button.
        """
        logout_button = tk.Button(self.root, text = "Se deconnecter", font=('Helvetica', 10, 'bold'), command=self.logout)
        logout_button.pack(pady=20)

    def logout(self):
        """
        Clears the screen and returns to the login page.
        """
        self.clear_screen()
        from models.login import LoginApp #Avoid cicular import between LoginApp and MemberHomePage
        LoginApp(self.root)
    

