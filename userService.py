import json
import os
from user import User

class UserService:
    def __init__(self, json_file="users.json"):
        self.json_file = json_file
        self.users = self.load_users()

    def load_users(self):
        if not os.path.exists(self.json_file):
            return[]
        with open(self.json_file, 'r') as file:
            users_data = json.load(file)
            users = []
            for user_data in users_data:
                user = User(
                    firstname = user_data.get("firstname", ""),
                    lastname = user_data.get("lastname", ""),
                    birthdate = user_data.get("birthdate", ""),
                    email = user_data.get("email", ""),
                    address = user_data.get("address", ""),
                    is_admin = user_data.get("is_admin", False)
                )

                user.user_id = user_data.get("user_id")
                users.append(user)
            return users
        
    def save_users(self):
        users_data = []
        for user in self.users:
            user_data = {
                "user_id" : user.user_id,
                "firstname" : user.firstname,
                "lastname" : user.lastnamme,
                "birthdate" : user.birthdate,
                "email" : user.email,
                "address" : user.address,
                "is_admin" : user.is_admin
            }
            
            users_data.append(user_data)

        with open(self.json_file, 'w') as file:
            json.dump(users_data, file, indent=4)

    def add_user(self, user):
        self.users.append(user)
        self.save_users()

    def get_users(self):
        return self.users
    
    def search_user(self, name):
        results = []
        for user in self.users:
            if name.lower() in f"{user.firstname} {user.lastname}".lower():
                results.append(user)
        return results