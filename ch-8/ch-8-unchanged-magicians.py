"""“
Unchanged Magicians: Start with your work from Exercise 8-10. 
Call the function make_great() with a copy of the list of magicians’ names. 
Because the original list will be unchanged, return the new list and store it in a separate list. 
Call show_magicians() with each list to show that you have one list of the original names and one list with the Great added to each magician’s name.”
"""

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians): ## MUST Change every entry in the list by index. Just doing for magician in magicians makes a temp copy of magician. 
                            ##Doesn't change the list that was passed
    for magician in range(len(magicians)):
        magicians[magician] += " The Great"
    return magicians

great_magicians = []
magicians = ["magician1","magician2","magician3","magician4"]
great_magicians = make_great(magicians[:]) ## Passes the list as a copy doesn't touch original list. 
show_magicians(magicians)
show_magicians(great_magicians)