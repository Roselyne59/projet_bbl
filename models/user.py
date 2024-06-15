class User:
    """_summary_

    Returns:
        _type_: _description_
    """
    user_number = 1

    def __init__(self, user_id, firstname, lastname, birthdate, email, street, zip_code, login, password, is_admin=False):
        """_summary_

        Args:
            user_id (_type_): _description_
            firstname (_type_): _description_
            lastname (_type_): _description_
            birthdate (_type_): _description_
            email (_type_): _description_
            street (_type_): _description_
            zip_code (_type_): _description_
            login (_type_): _description_
            password (_type_): _description_
            is_admin (bool, optional): _description_. Defaults to False.
        """
        self.user_id = user_id
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.email = email
        self.street = street
        self.zip_code = zip_code
        self.login = login
        self.password = password
        self.is_admin = is_admin
        if user_id >= User.user_number:
            User.user_number = user_id + 1

    def to_dict(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return {
            "user_id": self.user_id,
            "nom": self.firstname,
            "prenom": self.lastname,
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
        """_summary_

        Args:
            data (_type_): _description_

        Returns:
            _type_: _description_
        """
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