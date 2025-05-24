'''Write a while loop to asks why they like programming, add their reasons to a file'''
'''extra: add their name to the file'''
response_file_location = "/Users/vrodin/Documents/DEVELOPMENT/pythonPractice/PythonCrashCourse/ch-10/10-5/reason.txt"
while True:
    print("Enter your name and why you like to code. Type quit to quit\n" )

    user_name = input("Input your name: \n")
    if(user_name == "quit"):
        break
    user_response = input( user_name.title() + " why do you like to code? \n")
    if (user_response == "quit"):
        break
    with open(response_file_location,'a') as file:
        file.write(user_name.title() + " likes to code because: " + user_response + "\n")
    