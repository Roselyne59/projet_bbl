import json
import os
from user import User

class UserService:
    def __init__(self, json_file="users.json"):
        self.json_file = json_file
        self.users = self.load_users()

    def load_users(self):
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r') as file:
            users_data = json.load(file)
            return [
                User(**user_data)
                for user_data in users_data
            ]

    def save_users(self):
        with open(self.json_file, 'w') as file:
            json.dump([user.__dict__ for user in self.users], file, indent=4)

    def add_user(self, user):
        self.users.append(user)
        self.save_users()

    def get_users(self):
        return self.users

    def validate_credentials(self, login, password):
        for user in self.users:
            if user.login == login and user.password == password:
                return user
        return None
