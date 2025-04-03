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

print("list compreshension:")
squares = [myvalue **2 for myvalue in range(1,4)]
print(squares)

#count to 20
count  = []
for number in range(1,21):
    print(number)

#make a list of 1,000,000
count = list(range(1,1000001))
print(count)
print(min(count))
print(max(count))

multipleOfThree = list(range(3,31,3))
print(multipleOfThree)

cubed = [number**3 for number in range(1,11)]
print(cubed)

#slicing a list 
print("slicing a list")

myList = ['a','b','c','d','e']
print(myList[1:3])
print(myList[:4])
print(myList[2:])
print(myList[0])
x = "hello"[0]

print("looping through a slice.") 

for item in myList[0:4]:
    print(item)

#Copy a list

otherList = myList[:]
otherList.pop(-2)
otherList.append("Other list appended")
print(otherList)


otherList = myList
myList.append("3")
print(myList)
print(otherList)

#Tuples are lists you can't change but you can rewrite:
tupleA = (2,3,4)
#tupleA[1] = 2
for item in tupleA:
    print(item)

tupleA = (4,5,6)
print(tupleA)

#buffet problem

buffetTuple = ("eggs", "pizza", "pasta", "ice cream", "cookies")
#buffetTuple[0] = "othereggs"
for food in buffetTuple:
    print(food)

buffetTuple = ("cereal", "yogurt", "pasta", "ice cream", "cookies")
for food in buffetTuple:
    print(food)