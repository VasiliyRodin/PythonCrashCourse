#You first neeed to open the file
#Then you read it and assign what you read to object.
#Then you can work with object
file_path = "/Users/vrodin/Documents/DEVELOPMENT/pythonPractice/PythonCrashCourse/ch-10/first_file/file.txt"
with open(file_path) as file_object:
    contents = file_object.read()
    print(contents)