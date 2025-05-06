#“Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.”


print("Please input the pizza toppings you want. Once complete please type: quit")
pizzaToppingsList = []
pizzaTopping = ""
while pizzaTopping.lower() != "quit" :
    pizzaTopping = input("Please add a topping: ")
    if pizzaTopping.lower() != "quit":
        print("I will add " + pizzaTopping + " to the list. What else you would like to add?")
        pizzaToppingsList.append(pizzaTopping)

print("you have ordered the following toppings:")
for pizzaTopping in pizzaToppingsList:
    print (pizzaTopping)

