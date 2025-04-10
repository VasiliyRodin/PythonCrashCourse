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
