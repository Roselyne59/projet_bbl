import os
import json
from models.user import User


#It takes an optional parameter, default :json_file
class UserManager:
    """_summary_
    """
    def __init__(self, json_file="json/users.json"):
        """_summary_

        Args:
            json_file (str, optional): _description_. Defaults to "json/users.json".
        """
        self.json_file = json_file
        self.users = self.load_data()

    #load data from json file
    def load_data(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r') as file:
            return [User.from_dict(user) for user in json.load(file)]

    #save data in json file
    def save_data(self):
        """_summary_
        """
        with open(self.json_file, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file, indent=4)

    #Add new user
    def add_user(self, user):
        """_summary_

        Args:
            user (_type_): _description_
        """
        self.users.append(user)
        self.save_data()

    #Delete user
    def remove_user(self, user_id):
        """_summary_

        Args:
            user_id (_type_): _description_
        """
        self.users = [user for user in self.users if user.user_id != user_id]
        self.save_data()

    #Update existing user
    def update_user(self, new_user):
        """_summary_

        Args:
            new_user (_type_): _description_
        """
        for i, user in enumerate(self.users):
            if user.user_id == new_user.user_id:
                self.users[i] = new_user
                self.save_data()
                return

    #Check if login exists
    def login_exists(self, login):
        """_summary_

        Args:
            login (_type_): _description_

        Returns:
            _type_: _description_
        """
        return any(user.login == login for user in self.users)

    def get_user_by_login(self, login):
        for user in self.users:
            if user.login == login:
                return user
        return None

    def get_user_by_id(self, user_id):
        """_summary_

        Args:
            user_id (_type_): _description_

        Returns:
            _type_: _description_
        """
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None
