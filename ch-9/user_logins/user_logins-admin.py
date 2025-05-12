class User():
    def __init__(self,first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.login_attempts = 0
    
    def describe_user(self):
        print("First Name: " + self.first_name.title())
        print("Last Name: "+ self.last_name.title())
        print("Username: " + self.username)
        print("Email: " + self.email)

    def greet_user(self):
        full_name = str(self.first_name.title() + " " + self.last_name.title())
        print("Hello: " + full_name)
    
    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

class Admin(User):
    def __init__(self, first_name, last_name, username, email):
        super().__init__(first_name, last_name, username, email)
        self.privelages = ["view","modify","delete"]

    def show_privelages(self):
        print("This user has following privelages: ")
        for privelage in self.privelages:
            print(privelage)

admin_user = Admin("admin first","admin_last","admin_username","admin@admin.com")
admin_user.describe_user()
admin_user.show_privelages()
print("\n\n\n")

user1 = User("user1first","user2last","user1username", "user1@user1.com")
user1.describe_user()
user1.greet_user()


login_trys = 5
while login_trys != 0:
    user1.increment_login_attempts()
    login_trys -= 1
print("login attempts: " + str(user1.login_attempts))
user1.reset_login_attempts()
print("after reset: " + str(user1.login_attempts))

"""“Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166).
 Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 
 Write another method called reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times. 
Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). 
Print login_attempts again to make sure it was reset to 0.”
"""
