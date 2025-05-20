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