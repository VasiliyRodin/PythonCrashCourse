'''“Magicians: Make a list of magician’s names. 
Pass the list to a function called show_magicians(), which prints the name of each magician in the list.”'''

def show_magicians(magicians):
    for magician in magicians:
        print(magician)
        
magicians = ["magician1","magician2","magician3","magician4"]
show_magicians(magicians)
