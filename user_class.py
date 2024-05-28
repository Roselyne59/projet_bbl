class User:
    user_number = 0 # Class variable
    def __init__(self, firstname, lastname, birthdate,email,adress, is_admin=False):
        self.firstname = firstname
        self.lastname=lastname
        self.birthdate=birthdate
        self.email=email
        self.adress=adress
        self.user_id=User.user_number 
        User.user_number+=1 # Increment user ID after object creation
        self.is_admin = is_admin #distinguish admin

    def __str__(self):     #Representation
        user_type = "Admin" if self.is_admin else "Regular User"
        return f"{user_type}: {self.firstname} {self.lastname} (ID: {self.user_id})"


# Main code
user1 = User("Asloun", "Farid", "1982-10-10", "farid.asloun@example.com", "456 EQuartier des bonnes affaires, Syberie", is_admin=True)
user2 = User("Jean", "Mouloud", "1990-01-01", "Mouloud.jean@example.com", "123 Rue de la peine perdue")


print(user1)  
print(user2)  