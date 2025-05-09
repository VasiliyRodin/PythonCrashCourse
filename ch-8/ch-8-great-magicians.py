'''Great Magicians: Start with a copy of your program from Exercise 8-9. 
Write a function called make_great() that modifies the list of magicians by adding the phrase the Great to each magician’s name. 
Call show_magicians() to see that the list has actually been modified.”
'''
'''Although its the result. I had to make a new list. Not part of the instructions
def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians):
    while magicians:
        great_magicians.append(magicians.pop(0) + " the Great!")
        
magicians = ["magician1","magician2","magician3","magician4"]
great_magicians = []

make_great(magicians)
show_magicians(great_magicians)
'''

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

def make_great(magicians): ## MUST Change every entry in the list by index. Just doing for magician in magicians makes a temp copy of magician. 
                            ##Doesn't change the list that was passed
    for magician in range(len(magicians)):
        magicians[magician] += " The Great"
    return magicians

magicians = ["magician1","magician2","magician3","magician4"]
magicians = make_great(magicians)
show_magicians(magicians)