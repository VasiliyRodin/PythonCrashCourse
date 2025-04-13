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

#Looping through keys is the same as lists 
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
    new_alien = {'color': 'green', 'points':5, 'speed':'slow'}#dictionary gets created here
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


print("\n favorite languages example \n")

favorite_languages = {
    'judy':['c','c++','java'],
    'bobby':['java'],
    'susan':['python','C++']
}


for name,languages in favorite_languages.items(): # Watch out here, for loop with item keypair. Can call each one. 
    if len(languages) == 1:
        print("\n"+ name.title() + " Favorite language is: ")
        for language in languages:
                print(language.title()) 
    else:
        print('\n'+ name.title() + " Favorite languages are: ")
        for language in languages:
            print(language.title())


print("\n dictionary in a dictionary \n")

users = {
    'vrodin': {
        'first' : 'vasiliy',
        'last'  : 'rodin',
        'location' : 'california'
    },
    'bob':{
        'first':'bob',
        'last':'bobington',
        'location': 'europe'
    }
}

for username, user_info in users.items():
    user_full_name = user_info['first'] + " " + user_info['last']
    print('User with username: ' + username + "\n" + "Full name: " + user_full_name.title() + '\n' + user_info['location'].title())



print('\n\n\n Ch 6 practice: \n\n\n')
people = []
person_01 = {
    'first' :'bob',
    'last'  :'bobington',
    'age'   :'34',
    'city'  :'san jose'
}
person_02 = {
    'first' :'rob',
    'last'  :'robington',
    'age'   :'24',
    'city'  :'Ran Sose'
}
person_03 = {
    'first' :'tob',
    'last'  :'tobington',
    'age'   :'54',
    'city'  :'tan wose'
}
people.append(person_01)
people.append(person_02)
people.append(person_03)
for person in people:
    print("First Name: "+ person['first'].title() + " " + person['last'].title())
    print("\t Age: " + person['age'])
    print("\t Lives in city: " + person['city']) 



cities = {
    'san francisco':{
        'state': 'california',
        'population': 1000000,
        'weather': 'cold',
        'country': 'usa'
    },
    'miami': {
        'state': 'florida',
        'population': 4000000,
        'weather': 'too hot',
        'country': 'usa'
    }
}
print("Info on stored cities:")
for city, city_info in cities.items():
    print("this city name is: " + city.title())
    print('\t' + 'State: ' + city_info['state'].title())
    print('\t' + 'Population: ' + str(city_info['population']))
    print('\t' + 'Weather' + city_info['weather'])
    print('\t' + 'Country: ' + city_info['country'])



