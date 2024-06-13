class User:
    user_number = 1

    def __init__(self, user_id, nom, prenom, birthdate, email, street, zip_code, login, password, is_admin=False):
        self.user_id = user_id
        self.nom = nom
        self.prenom = prenom
        self.birthdate = birthdate
        self.email = email
        self.street = street
        self.zip_code= zip_code
        self.login = login
        self.password = password
        self.is_admin = is_admin
        if user_id >= User.user_number:
            User.user_number = user_id + 1

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "nom": self.nom,
            "prenom": self.prenom,
            "date_de_naissance": self.birthdate,
            "email": self.email,
            "rue": self.street,
            "code_postal": self.zip_code,
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
            data["rue"],
            data["code_postal"],
            data["login"],
            data["password"],
            data.get("is_admin", False)
        )