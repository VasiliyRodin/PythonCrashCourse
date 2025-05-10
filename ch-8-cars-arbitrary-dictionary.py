"""“8-14. Cars: Write a function that stores information about a car in a dictionary. 
The function should always receive a manufacturer and a model name. It should then accept an arbitrary number of keyword arguments. 
Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 
Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was stored correctly.”
"""


def make_car(make, model, year, **packages):
    car = {}
    car["make"] = make
    car["model"] = model
    car["year"] = year
    for package, selection in packages.items():
        car[package] = selection
    return car


car = make_car('subaru','outback', 2011 ,color ="blue", tow_package=True, tint_package=True)
for key, value in car.items():
    print (key + " " + str(value) )