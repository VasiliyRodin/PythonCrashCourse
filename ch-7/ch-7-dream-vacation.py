#“Write a program that polls users about their dream vacation. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.


responses = {}  # Will have names and locations. Users can have multiple locations:

polling_isActive = True

while polling_isActive:
    name = input("Please enter your name and hit enter: ")
    dream_visit = input("If you could visit one place where would you like to go: ")
    responses[name] = dream_visit
    """ Incorrect
    run_again_active = True
    while run_again_active:
        run_again = input("Does anyone else want to add their dream visit? yes/no: ")    
        if run_again.lower() == "no":
            polling_isActive = False
            run_again_active = False
        if run_again.lower != "yes":
            print("Please enter yes or no")
    """
    while True: ##This runs every time with the following conditions. The breaks quit out this loop only. 
        run_again = input("Does anyone else want to add their dream visit? yes/no: ")
        if run_again.lower() == "no":
            polling_isActive = False
            break
        elif run_again.lower() == "yes":
            break
        else:
            print("Please enter yes or no")

for name, dream_visit in responses.items(): ### NEED TO REMEMBER TO ADD .items to a dictionarry
    print(" " + name.title() + " wants to visit " + dream_visit.title())




