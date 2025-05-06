#“Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.”

sandwich_orders = ["Tuna", "Pastrami", "Ham & Cheese", "Turkey Club", "Pastrami","Royal with Cheese", "Hula Sandwich", "Pastrami"]
finished_sandwiches = []
#len won't work since pastrami is out.
#Never modify a list while iterating over it with a for loop. REMEMBER
while sandwich_orders:
    sandwich = sandwich_orders.pop(0) #Pops the first one in the list
    if sandwich.lower() == "pastrami":
        print("We are out of Pastrami")
    else:
        print("I made your " + sandwich)
        finished_sandwiches.append(sandwich)

print("List of compelted sandwiches" + str(finished_sandwiches))


