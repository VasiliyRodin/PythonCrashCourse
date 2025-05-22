"""“Make a class Die with one attribute called sides, which has a default value of 6. 
Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. 
Make a 6-sided die and roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.”
"""


from random import randint

class Die():
    def __init__(self, sides = 6):
        self.sides = sides

    def rollDie(self):
        print("Your " + str(self.sides) + " sided dice rolled a " + str(randint(1,self.sides)))

die_6 = Die()
for _ in range(10):
    die_6.rollDie()
die_10 = Die(sides=10)
for _ in range(10):
    die_10.rollDie()


