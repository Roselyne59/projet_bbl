import os
import json
from models.user import User


class UserManager:
    """
        Manager class for handling user records.

        Attributes:
            json_file (str): Path to the JSON file where user records are stored.
            users (list): List of User objects.
        """
    def __init__(self, json_file="json/users.json"):
        """
        Initializes the UserManager with the given JSON file path.

        Args:
            json_file (str, optional): Path to the JSON file. Defaults to "json/users.json".
        """
        self.json_file = json_file
        self.users = self.load_data()

    def load_data(self):
        """
        Loads user data from the JSON file.

        Returns:
            list: A list of User objects.
        """
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r') as file:
            return [User.from_dict(user) for user in json.load(file)]

    def save_data(self):
        """
        Saves the current user data to the JSON file.
        """
        with open(self.json_file, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file, indent=4)

    def add_user(self, user):
        """
        Adds a new user record and saves the updated list to the JSON file.

        Args:
            user (User): The user record to add.
        """
        self.users.append(user)
        self.save_data()

    def remove_user(self, user_id):
        """
         Removes a user record by its ID and saves the updated list to the JSON file.

         Args:
             user_id (int): The ID of the user record to remove.
         """
        self.users = [user for user in self.users if user.user_id != user_id]
        self.save_data()

    def update_user(self, new_user):
        """
        Updates an existing user record and saves the updated list to the JSON file.

        Args:
            new_user (User): The updated user record.
        """
        for i, user in enumerate(self.users):
            if user.user_id == new_user.user_id:
                self.users[i] = new_user
                self.save_data()
                return

    def login_exists(self, login):
        """
        Checks if a login name already exists.

        Args:
            login (str): The login name to check.

        Returns:
            bool: True if the login name exists, False otherwise.
        """
        return any(user.login == login for user in self.users)

    def get_user_by_login(self, login):
        """
                Retrieves a user record by its login name.

                Args:
                    login (str): The login name of the user.

                Returns:
                    User: The user record with the given login name, or None if not found.
                """
        for user in self.users:
            if user.login == login:
                return user
        return None

    def get_user_by_id(self, user_id):
        """
        Retrieves a user record by its ID.

        Args:
            user_id (int): The ID of the user.

        Returns:
            User: The user record with the given ID, or None if not found.
        """
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
