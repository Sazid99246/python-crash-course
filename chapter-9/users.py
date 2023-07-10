class User():
    def __init__(self, first_name, last_name, age, location, email, username):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.username = username
        self.login_attempt = 0

    def describe_user(self):
        print("\nFirst name: " + self.first_name.title())
        print("Last name: " + self.last_name.title())
        print("Email: " + self.email)
        print("Username: " + self.username)
        print("Age: " + str(self.age))
        print("Location: " + self.location)

    def greet_user(self):
        print("\nWelcome to the board, " + self.first_name.title())

    def incremental_login_attempts(self):
        self.login_attempt += 1
    
    def reset_login_attempt(self):
        self.login_attempt = 0

sazid = User("sazidul", "islam", 23, "Dhaka, Bangladesh", "sheikhmdsazidulislam@gmail.com", "sazid991")
sazid.describe_user()
sazid.greet_user()
sazid.incremental_login_attempts()
sazid.incremental_login_attempts()
sazid.incremental_login_attempts()
sazid.incremental_login_attempts()
sazid.incremental_login_attempts()
print(sazid.login_attempt)
sazid.reset_login_attempt()
print(sazid.login_attempt)

# lazz = User("sanja", "lazz", 19, "Dhaka, Bangladesh", "sanja554@gmail.com", "sanja554")
# lazz.describe_user()
# lazz.greet_user()


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

sazid = Admin("sazidul", "islam", 23, "Dhaka, Bangladesh", "sheikhmdsazidulislam@gmail.com", "sazid991")
sazid.show_privileges()  # This will display the admin privileges
sazid.privileges.privileges = ["can add post", "can edit post", "can delete post", "can add user", "can remove user", "can ban user", "can update user profile", "can make a group", "can delete group", "can update group status", "can remove any member from any group"]
sazid.show_privileges()  # This will display the updated admin privileges
