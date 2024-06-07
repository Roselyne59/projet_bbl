import os
import json
from user import User


class UserManager:
    def __init__(self, json_file="users.json"):
        self.json_file = json_file
        self.users = self.load_data()

    def load_data(self):
        if not os.path.exists(self.json_file):
            return []
        with open(self.json_file, 'r') as file:
            return [User.from_dict(user) for user in json.load(file)]

    def save_data(self):
        with open(self.json_file, 'w') as file:
            json.dump([user.to_dict() for user in self.users], file, indent=4)

    def add_user(self, user):
        self.users.append(user)
        self.save_data()

    def remove_user(self, user_id):
        self.users = [user for user in self.users if user.user_id != user_id]
        self.save_data()

    def update_user(self, new_user):
        for i, user in enumerate(self.users):
            if user.user_id == new_user.user_id:
                self.users[i] = new_user
                self.save_data()
                return

    def login_exists(self, login):
        return any(user.login == login for user in self.users)