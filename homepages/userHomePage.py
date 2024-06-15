import tkinter as tk

class UserHomePage:
    def __init__(self, root, firstname, lastname):
        self.root = root
        self.clear_screen()
        
        self.welcome_message(firstname, lastname)
        self.logout_bouton()

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def welcome_message(self, firstname, lastname):
        welcome_message= f"Bienvenue {firstname} {lastname}"
        welcome_label = tk.Label(self.root, text = welcome_message, font=('helvetica', 16, 'bold'), fg='red')
        welcome_label.pack(pady=20)
    
    def logout_bouton(self):
        logout_button = tk.Button(self.root, text = "Se deconnecter", font=('Helvetica', 10, 'bold'), command=self.logout)
        logout_button.pack(pady=20)

    def logout(self):
        self.clear_screen()
        from models.login import LoginApp #Avoid cicular import between LoginApp and MemberHomePage
        LoginApp(self.root)
    

