class User:
    user_number = 0

    def __init__(self, firstname, lastname, birthdate, login, password, email, address, is_admin=False, user_id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.login = login
        self.password = password
        self.email = email
        self.address = address
        self.is_admin = is_admin
        if user_id is None:
            self.user_id = User.user_number
            User.user_number += 1
        else:
            self.user_id = user_id
            User.user_number = max(User.user_number, user_id + 1)

    def __str__(self):
        user_type = "Admin" if self.is_admin else "Regular User"
        return f"{user_type}: {self.firstname} {self.lastname} (ID: {self.user_id})"
