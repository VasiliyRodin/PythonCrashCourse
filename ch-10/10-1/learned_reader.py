
'''Print contents once by reading in the entire file.
once by looping over the file object and 
once by storing the lines in a list and then working with them outside the with block.'''

file_location = "/Users/vrodin/Documents/DEVELOPMENT/pythonPractice/PythonCrashCourse/ch-10/10-1/learning_python.txt"

with open(file_location) as text:
    my_learnings = text.read()
    print(my_learnings)


with open(file_location) as looping_example:
    for line in looping_example:
        print(line.rstrip())

print('\n')

with open(file_location) as lines:
    my_lines = lines.readlines()

for line in my_lines:
    print(line.rstrip())
print(len(my_lines))