'''
“
Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 
Make a method called describe_restaurant() that prints these two pieces of information, 
and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.”
'''


class Restaurant():
    def __init__(self,restaurant_name, restaurant_type):
        self.name = restaurant_name
        self.type = restaurant_type

    def describe_restaurant(self):
        print("Restaurant name: " + self.name.title())
        print("Restaurant type: " + self.type.title())
    
    def open_restaurant(self):
        print("Restaurant " + self.name.title() + " opens at 6pm")

my_restaurant = Restaurant("bobs place","french")

my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

restaurant2 = Restaurant("Name2", "type2")
restaurant2.describe_restaurant()

restaurant3 = Restaurant("Name3", "type3")
restaurant3.describe_restaurant()

