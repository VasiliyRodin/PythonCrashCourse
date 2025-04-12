#Dictionaries
alien_example = {'color': "Blue", 'size': "large"}

print(alien_example['color'])
print(alien_example['size'])

#Adding new stuff to dicitionary:

alien_example['damage'] = 5
alien_example['health'] = 100
print(alien_example)

#starting with a blank dictionary
player_example = {}
player_example['health'] = 100

print(player_example)

#modify data (health damage)
player_example['health'] -= alien_example['damage']
print(player_example['health'])


#Removing key value pair:

del player_example['health']
print(player_example)

player_example['health'] = 100
print(player_example)


favorite_foods = {
    "bob"       : "pizza",
    "sarah"     : "burgers",
    "rod"       : "cake",
    "jim"       : "jello"
}
print("Jims favorite food is:" + favorite_foods['jim'])


print("Going through a dictionary")

favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python'}

for name in favorite_languages:
    print(name.title())

#Looping through keys is the same as 
for name in favorite_languages:
    print(name.title())

print('\n')


favorite_languages = {'jen': 'python','sarah': 'c','edward': 'ruby','phil': 'python'}
friends_list = ['sarah', 'phil']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends_list: #checks if name is in the list of friends
        print("Hi " + name.title() + " your favorite language is: " + favorite_languages[name].title())
    print("\n")
    if 'edward' not in favorite_languages.keys():
        print("I correctly got edward")

print("this is for the sorted list")
for name in sorted(favorite_languages.keys()):
    print(name)
    print("Sort the list of keys first them print them")


print("\nLooking through all values of a dictionary")
print("Following languages have been mentioned: \n")
for language in sorted(favorite_languages.values()):
    print(language)


print("\n Glossary example")
glossary = {
            'tuple':"A list thats immuatble",
            'list':"Pretty much an array a collection of items.",
            'for': "A kind of loop for each something in another something",
            'if': "Another kind of loop. If something is or isn't do this"
            }
for term in glossary:
    print(term.title() + " is " + glossary[term])



print("\n Lists of dictionaries Create a list of aliens and fill them up with alien dictionary")

alien = [] #empty list
#make 30 aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points':5, 'speed':'slow'}
    alien.append(new_alien) #adds the alien to the empty list. 
for aliens in alien[:5]:
    print(aliens)

print("Total amount of aliens " + str(len(alien)))




#Lists in a dictionary
print("\n list in dictionary")

pizza = {
    'crust':'Thick',
    'toppings': ['pep','ham','pineapple']
}
print("Your pizza crust is: " + pizza['crust'] +'\n')
print("your toppings are:")
for topping in pizza['toppings']:
    print(topping)

    