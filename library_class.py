class Library:
    def __init__(self):
        self.users = []  # Users list

    def user_add(self,user):    # adding user
        self.users.append(user)

    def user_list_show(self):   #Dislplays users list
        for user in self.users:
            print(f'User Id : {user.user_id}, Name : {user.firstname} {user.firstname} {user.is_admin}')
    
    def user_search(self, name): #user search by name
        results = []            #Search results
        for user in self.users:
            if name.lower() in user.name.lower():
                results.append(user)
        return results


    
