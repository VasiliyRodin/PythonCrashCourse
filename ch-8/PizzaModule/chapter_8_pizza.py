def make_pizza(size, *toppings):
    "summarize the pizza we are making"
    print("We are making a pizza with size: "+ str(size) + " with toppings: ")
    for topping in toppings:
        print(topping)