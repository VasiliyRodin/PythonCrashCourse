#“Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.”

def  make_shirt(size, tshirt_text):
    print("This shirt is size " + size + " with the text: " + tshirt_text)

#positional arguments
make_shirt("small", "cool text on shirt")
#keyword arguments
make_shirt(size = "Large", tshirt_text="This is a cool shirt")

#“Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.”

def make_shirts2(tshirt_text,size='large'):
    print("default size of this shirt is " + size + " with text " + tshirt_text)
make_shirts2("Python is cool",) ## can change the size by adding "small"



#“Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.”

def describe_city(city_name, country="USA"):
    print(city_name.title() + " is located in " + country)
describe_city("New York")
describe_city(city_name="Moscow", country="RF")
describe_city("Berlin", "Germany")

