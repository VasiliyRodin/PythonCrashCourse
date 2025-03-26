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

age = 13
admission_age = 0

if age < 4:
    admission_price = 4
elif age >= 4 and age < 16:
    admission_price = 13
else:
    admission_price = 19
print("your age: " + str(age) + " price is: " + str(admission_price))



print("Try yourself \n")
alien_color = "red"
if alien_color == "green":
    print("you earned 5 points")
if alien_color == "yello":
    print("You earned 10 points")
elif alien_color == "red":
    print("you earned 13 points")   



toppings_list = ["Chicken", "Peppers", "Olives", "Ham"]

for topping in toppings_list:
    if topping == "Chicken":
        print("what are you nuts?")


#Checking empty list

mylist = []
if len(mylist) == 0 :
    print("this thing is empty")


user_names = ["admin" , "bob", "sue", "nick", "tom","peggy"]
if len(user_names) != 0:
    for user in user_names:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print("Hello user: " + user)
else:
    print("no user in list")


current_users = ["Bob", "Sue", "Nick", "Tom","Peggy","Rob","Jen"]
new_users = ["Jim", "PEGGY","Steve","Sally","Tom","SAM"]

for new_user in new_users:
    if new_user.title() in current_users:
        print("Name " + new_user + " is not available")
    else:
        print (new_user + " is available")