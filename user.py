class User:
    user_number = 0
    def __init__(self, firstname, lastname, birthdate, email, address, is_admin=False):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.email = email
        self.address = address
        self.user_id = User.user_number
        User.user_number+=1
        self.is_admin = is_admin

    def __str__(self):
        user_type = "Admin" if self.is_admin else "Regular User"
        return f"{user_type}: {self.firstname} {self.lastname} (ID: {self.user_id})"