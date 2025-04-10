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


for name in favorite_languages:
    if name == "sarah"