class Dog():
    #Model of a dog it has name age and can method(roll over and sit) (at the moment we don't have an instance of dog)
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def dog_sit(self):
        print(self.name.title() + " is sitting")
    def dog_roll_over(self):
        print(self.name.title() + " is rolling over")



##Making the dog instance here:
my_dog = Dog("willy", 12)
print("Dogs name: " + my_dog.name.title())
print("Dogs age: " + str(my_dog.age))

my_dog.dog_roll_over()
my_dog.dog_sit()


your_dog = Dog("bobby",3)
print("Your dogs name: " + your_dog.name)
print("Your dogs age: " + str(your_dog.age))

your_dog.dog_sit()
your_dog.dog_roll_over()

