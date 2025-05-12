'''“Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 166)
 or Exercise 9-4 (page 171). Either version of the class will work; just pick the one you like better. 
 Add an attribute called flavors that stores a list of ice cream flavors. 
 Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.”
'''

class Restaurant():
    def __init__(self,restaurant_name, restaurant_type):
        self.name = restaurant_name
        self.type = restaurant_type
        self.number_served = 0

    def describe_restaurant(self):
        print("Restaurant name: " + self.name.title())
        print("Restaurant type: " + self.type.title())
    
    def open_restaurant(self):
        print("Restaurant " + self.name.title() + " opens at 6pm")

    def set_number_served(self, num_of_customers_served):
        self.number_served = num_of_customers_served
    
    def increment_number_served(self, increment):
        self.number_served += increment

###NEW CLASS ###
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, restaurant_type):
        super().__init__(restaurant_name, restaurant_type)
        self.flavors = ["Flav1","Flav2","Flav3","Flav4","Flav5"]
    def display_flavors(self):
        print("this is to print every flavor we have")
        for type in self.flavors:
            print(type)


restaurant = Restaurant("bobs place","french")
print("Number of people served: "+ str(restaurant.number_served))
restaurant.number_served = 50
print("Number of people served: "+ str(restaurant.number_served))
restaurant.set_number_served(100)
print("Number of people served: "+ str(restaurant.number_served))
restaurant.increment_number_served(5)
restaurant.increment_number_served(1)
restaurant.increment_number_served(7)
print("Number of people served: "+ str(restaurant.number_served))
print('\n\n\n')
myIceCreamStand = IceCreamStand("My Stand", "ice cream")
myIceCreamStand.describe_restaurant()
myIceCreamStand.display_flavors()