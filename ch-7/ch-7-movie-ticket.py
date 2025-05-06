#“A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.”

#Program wont end until "cart" is input


# Ask how many under 3, ask how many 3-12, ask how many over 12

print("Movie ticket prices: \n Persons under 3: \t\tFree Admission \n Persons between 3 and 12 : \t$10 \n Persons over 12: \t\t$15")
print("\n Please your age to see your price, once completed type in quit")
ageInput=""
while True:
    ageInput = input("Pleae enter your age: ")
    if ageInput.lower() == "quit":
        print("You typed quit")
        break
    age = int(ageInput)
    if age < 3:
        print("your ticket is free")
    if age >= 3 and age < 12:
        print("your ticket is 10$")
    if age >= 12:
        print("Your ticket is 15$")
    