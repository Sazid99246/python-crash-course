from users import User

class Admin(User):
    def __init__(self, first_name, last_name, age, location, email, username):
        super().__init__(first_name, last_name, age, location, email, username)
        self.privileges = Privileges()  # Create an instance of Privileges class
    
    def show_privileges(self):
        """Shows the admin privileges"""
        self.privileges.show_privileges()  # Call the show_privileges method of Privileges

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        if self.privileges:
            for privilege in self.privileges:
                print(" -" + privilege)
        else:
            print("The user has no privileges")