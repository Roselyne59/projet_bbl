class User:
    user_number = 1

    def __init__(self, user_id, firstname, lastname, birthdate, email, address, login, password, is_admin=False):
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.email = email
        self.address = address
        self.login = login
        self.password = password
        self.is_admin = is_admin
        if user_id >= User.user_number:
            User.user_number = user_id + 1

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "nom": self.firstname,
            "prenom": self.lastname,
            "date_de_naissance": self.birthdate,
            "email": self.email,
            "adresse": self.address,
            "login": self.login,
            "password": self.password,
            "is_admin": self.is_admin
        }

    @staticmethod
    def from_dict(data):
        return User(
            data["user_id"],
            data["nom"],
            data["prenom"],
            data["date_de_naissance"],
            data["email"],
            data["adresse"],
            data["login"],
            data["password"],
            data.get("is_admin", False)
        )