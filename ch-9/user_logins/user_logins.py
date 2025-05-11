class User():
    def __init__(self,first_name, last_name, username, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
    
    def describe_user(self):
        print("First Name: " + self.first_name.title())
        print("Last Name: "+ self.last_name.title())
        print("Username: " + self.username)
        print("Email: " + self.email)

    def greet_user(self):
        full_name = str(self.first_name.title() + " " + self.last_name.title())
        print("Hello: " + full_name)

user1 = User("user1first","user2last","user1username", "user1@user1.com")
user1.describe_user()
user1.greet_user()

