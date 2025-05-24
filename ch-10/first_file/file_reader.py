#You first neeed to open the file
#Then you read it and assign what you read to object.
#Then you can work with object
file_path = "/Users/vrodin/Documents/DEVELOPMENT/pythonPractice/PythonCrashCourse/ch-10/first_file/file.txt"
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)
print("\n")

with open(file_path) as file_obj_name:
    for line in file_obj_name:
        print(line.rstrip())
#rstrip() deletes whitespaces


print("\n\n\n")
"Takes the contents line by line and adds them to a list"
my_list = []
with open(file_path) as listOfNames:
    for name in listOfNames:
        my_list.append(name.rstrip())
    print(my_list)



with open(file_path) as pi:
    lines = pi.readlines()
py_string = ""
for lines in lines:
    py_string += lines.strip()

print(py_string)
print(len(py_string))