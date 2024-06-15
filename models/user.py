class User:
    """
        Class representing a user.

        Attributes:
            user_id (int): The ID of the user.
            firstname (str): The first name of the user.
            lastname (str): The last name of the user.
            birthdate (str): The birthdate of the user.
            email (str): The email address of the user.
            street (str): The street address of the user.
            zip_code (str): The zip code of the user's address.
            login (str): The login name of the user.
            password (str): The password of the user.
            is_admin (bool): Indicates if the user has admin privileges. Defaults to False.
        """
    user_number = 1

    def __init__(self, user_id, firstname, lastname, birthdate, email, street, zip_code, login, password, is_admin=False):
        """
        Initializes a User object.

        Args:
            user_id (int): The ID of the user.
            firstname (str): The first name of the user.
            lastname (str): The last name of the user.
            birthdate (str): The birthdate of the user.
            email (str): The email address of the user.
            street (str): The street address of the user.
            zip_code (str): The zip code of the user's address.
            login (str): The login name of the user.
            password (str): The password of the user.
            is_admin (bool, optional): Indicates if the user has admin privileges. Defaults to False.
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
        """
        Converts the User object to a dictionary.

        Returns:
            dict: A dictionary representation of the User object.
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
        """
        Creates a User object from a dictionary.

        Args:
            data (dict): A dictionary containing user data.

        Returns:
            User: A User object created from the dictionary data.
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