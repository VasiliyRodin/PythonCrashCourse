magicians = ["bob", "alice", "luke"]

#not good. still breaks.
for magician in magicians:
    print (magician)

    print("thank you")

fav_pizza = ['pep','cheese','combo']

for pizza in fav_pizza:
    print("I like " + pizza + " pizza")

print("I really like pizza")


#Range function that generates series of numbers
#prints 1-3
for value in range(1,4):
    print(value)

print("Other value")
print("Odd numbers")
for value in range(1,19,2):
    print(value)
print("Even numbers")
for value in range(2,21,2):
    print(value)


print("usng range to make a list of numbers using list()")
value = list(range(1,31,2))
print(value)


print("squaring stuff")
squares = []
for value in range(1,19,2):
    squares.append(value**2)

print(squares)

print(min(squares))
print(max(squares))
print(sum(squares))