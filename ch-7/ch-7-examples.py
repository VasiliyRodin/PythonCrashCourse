###“Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.”

car_choice = input("Please enter the brand of car you want to rent: \n")
print("Searching cars that are "+ car_choice + "'s")

### “Restaurant Seating: Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message saying they’ll have to wait for a table. Otherwise, report that their table is ready.”

party_size = int(input("Please enter the amount of guests in your party: "))

if party_size >= 8:
    print("You will have to wait")
else:
    print("Your table is ready")

### “Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

number_to_check = int(input("Please enter a number to check if it is amultiple of 10:\n"))
if (number_to_check % 10) == 0: ## Checks for no remainder
    print("Number " + str(number_to_check) +" is a multiple of 10")
else:
    print("Number " + str(number_to_check) +" is not a multiple of 10")
