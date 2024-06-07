import json
import os
from user import User

class UserService:
    def __init__(self, json_file="json/users.json"):
        self.json_file = json_file
        self.users = self.load_users()

    def load_users(self):
        if not os.path.exists(self.json_file):
            return []
        try:
            with open(self.json_file, 'r') as file:
                users_data = json.load(file)
                return [
                    User(**user_data)
                    for user_data in users_data
                ]
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error loading users: {e}")
            return []

    def save_users(self):
        try:
            with open(self.json_file, 'w') as file:
                json.dump([user.__dict__ for user in self.users], file, indent=4)
        except IOError as e:
            print(f"Error saving users: {e}")

    def add_user(self, user):
        if not self.is_login_taken(user.login):
            self.users.append(user)
            self.save_users()
        else:
            print(f"Login {user.login} already taken")

    def get_users(self):
        return self.users

    def validate_credentials(self, login, password):
        for user in self.users:
            if user.login == login and user.password == password:
                return user
        return None

    def is_login_taken(self, login):
        return any(user.login == login for user in self.users)
