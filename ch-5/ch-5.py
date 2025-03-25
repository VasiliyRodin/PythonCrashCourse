mylist = ['a', 'b', 'c' , 'd', 'e']

for item in mylist:
    if item == 'b' :
        print("this is " + item)
    else:
        print("this is not 'b")


# and or
age_0 = 19
age_1 = 23

if age_0 == 19 and age_1 > age_0:
    print("test")

if age_0 == 19 or age_1 <= age_0:
    print("test2")

#Checking value in a list

requested_topping = ["pep", "pepper", "olives"]
topping = "ham"
if "cheese" in requested_topping:
    print("cheese in toping list")
else:
    print("no cheese")

if topping not in requested_topping:
    print(topping + " not in list")
