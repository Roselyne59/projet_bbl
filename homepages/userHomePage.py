import tkinter as tk

class UserHomePage:
    """_summary_
    """
    def __init__(self, root, firstname, lastname):
        """_summary_

        Args:
            root (_type_): _description_
            firstname (_type_): _description_
            lastname (_type_): _description_
        """
        self.root = root
        self.clear_screen()
        
        self.welcome_message(firstname, lastname)
        self.logout_bouton()

    def clear_screen(self):
        """_summary_
        """
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def welcome_message(self, firstname, lastname):
        """_summary_

        Args:
            firstname (_type_): _description_
            lastname (_type_): _description_
        """
        welcome_message= f"Bienvenue {firstname} {lastname}"
        welcome_label = tk.Label(self.root, text = welcome_message, font=('helvetica', 16, 'bold'), fg='red')
        welcome_label.pack(pady=20)
    
    def logout_bouton(self):
        """_summary_
        """
        logout_button = tk.Button(self.root, text = "Se deconnecter", font=('Helvetica', 10, 'bold'), command=self.logout)
        logout_button.pack(pady=20)

    def logout(self):
        """_summary_
        """
        self.clear_screen()
        from models.login import LoginApp #Avoid cicular import between LoginApp and MemberHomePage
        LoginApp(self.root)
    

