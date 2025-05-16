'''“Let’s create a module containing just the Car class.'''

class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def describe_car(self):
        full_name = ("This car make: " + self.make + " This car model: "+ self.model + " This car year: " + str(self.year))
        return full_name