"""Every attribute in a class needs an initial value, even if that value is 0 or an empty string. 
In some cases, such as when setting a default value, it makes sense to specify this initial value in the body of the __init__() method; 
if you do this for an attribute, you don’t have to include a parameter for that attribute.”
"""

'''“We can extend the method update_odometer() to do additional work every time the odometer reading is modified.
 Lets add a little logic to make sure no one tries to roll back the odometer reading:”
'''
#The parameter that changes is odometer. 
class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        ###Not something thats passed but can be created manually and changed later
        self.odometer = 15
    
    def car_description(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    def read_odometer(self):
        print("the cars current odometer reading is: " + str(self.odometer) + "miles")
    
    def update_odometer(self, updated_odometer_reading):
        if self.odometer <= updated_odometer_reading:
            self.odometer = updated_odometer_reading
        else:
            print("You are reverting odometer")

new_car = Car("honda", "civic", 2005)   
#new_car.odometer = 50 Using a method instead to update the odometer
print(new_car.car_description())
new_car.update_odometer(14)
new_car.read_odometer()