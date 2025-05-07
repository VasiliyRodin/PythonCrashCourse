'''“Write a function called city_country() that takes in the name of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value that’s returned.”
'''

def city_country(city, country):
    city_format = str(city.title() + ", " + country.title())
    return city_format

print(city_country("san fsrancisco", "united states"))
print(city_country("moscow", "russia"))
print(city_country("tokyo", "japan"))

