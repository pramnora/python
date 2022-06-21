#-----------------------------------
# Computer: Desktop PC/Windows 10 Professional
# Language: Python, Version: 3.10.0
#  Program: Find age status
#-----------------------------------
#   Author: Paul Ramnora
#    Email: pramnora@yahoo.com
#-----------------------------------
#  Created: 210622 14:14 PM GMT
#  Updated: 210622 14:14 PM GMT
#-----------------------------------

# Initialise variables...

age=0;

# Main Program...

while(age>=0):

    age = int(input("(Type '-1' to stop...)/What is your age? "))
    ageStatus = ""

    if (age>=0 and age<10):
        ageStatus="child"
    elif (age>=10 and age<18):
        ageStatus="teenager"
    elif (age >=18 and age <21):
        ageStatus="young adult"
    else:
        ageStatus="full adult"

    if (age<0):
        print("-Thanks! Program finished!")
    else:
        print("You are ", age, "years old; therefore, you are a " + ageStatus)
