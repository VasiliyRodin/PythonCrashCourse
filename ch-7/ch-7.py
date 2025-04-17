some_text = ''
print("please input some text: ")
some_text = input() 
print("You typed: " + some_text)


another_text = input("Plase put some text and ill copy it: ")
print(another_text)

prompt = "This program copies stuff and adds the prompt to the output"
prompt += "This is another thign getting added to the prompt"
name = input(prompt)
print('\n' + name)




print('\n \n\n using int() for inputing numbers only')

prompt = "Please enter your age: "
older_prompt = "You are over 18"
yunger_prompt = "You are under 18"
age = input(prompt)
age = int(age)
if age >= 18:
    print(older_prompt)
else:
    print(yunger_prompt)



cat_weight = input("Please enter the amount your cat weighs in pounds: ")
cat_weight = float(cat_weight)
cat_calories = (cat_weight // 1) * 20 #floor division how many times for every cat pound add 20 calories
print("your cat should consume " + str(cat_calories) + " calories")

