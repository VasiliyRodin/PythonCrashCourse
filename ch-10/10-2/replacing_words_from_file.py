''' Read in each line from the file and replace Python with another language'''

file_location = "/Users/vrodin/Documents/DEVELOPMENT/pythonPractice/PythonCrashCourse/ch-10/10-2/learning_python.txt"

with open(file_location) as file:
    my_learnings = file.readlines()
word_find = "Python"
count = 0
for line in my_learnings:
    count += line.count(word_find)
    line = line.replace('Python','C')
    print(line)
print(count)