"""Prompt the user for a name and them export to a file."""
file_path = "ch-10/10-3/guests.txt"

while True:
    name = input("Please enter a name. To exit type exit ")
#### using w overwrites the old file. a appends.
    with open(file_path,'a') as my_file:
        my_file.write(name + "\n")
    if name == "exit":
        break