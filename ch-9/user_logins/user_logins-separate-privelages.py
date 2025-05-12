'''“Write a separate Privileges class. The class should have one attribute, privileges, 
that stores a list of strings as described in Exercise 9-7. 
Move the show_privileges() method to this class. 
Make a Privileges instance as an attribute in the Admin class.
 Create a new instance of Admin and use your method to show its privileges.”
'''
class Privilege():
    def __init__(self,privilege_list =["view","modify","delete"]):
        self.privileges = privilege_list
    def show_privileges(self):
        print("This user has following privileges: ")
        for privileges in self.privileges:
            print(privileges)

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
        self.privilege = Privilege()

        


admin_user = Admin("admin first","admin last","admin_username","admin@admin.com")
admin_user.describe_user()
admin_user.privilege.show_privileges()
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

