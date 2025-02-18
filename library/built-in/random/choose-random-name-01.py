# ------------------------------------------
# Created: Tue 180225 11:25 AM GMT
# Updated: Tue 180225 11:25 AM GMT
# ------------------------------------------
# WHAT THE PROGRAM DOES
# Demonstrates the use of Python library: 
# random/choice
# ------------------------------------------
# CREDITS: Program borrowed from Skillshare course...
# Coding 101: Python for Beginners, 
# Teacher: Alvin Wan, Research Scientist
# URL: 
# https://www.skillshare.com/en/classes/coding-101-python-for-beginners/973997848/classroom
# ------------------------------------------

# choice, selects data 'randomly' from a list of multiple choices
from random import choice
# print user instructions
print("-----------------------------------------------------------")
print("PROGRAM: Random name selector")
print("-----------------------------------------------------------")
print("USER INSTRUCTIONS: ")
print()
print("After being given a list of multiple names...;")
print("this program will select a 'random name' from the list.")
print()
print("NOTE: Type in multiple names...;")
print("      and, with each successive name being comma separated:")
print("      name1,name2,name3,-etc.")
print("      Finally, press [ENTER] key when done.")
print("-----------------------------------------------------------")
# get user to type in their response
response = input("Names: ")
# the users response is listed into a comma separated array
names = response.split(",")
# print out the comma separated array list
print()
print("Here is the list you did originally type in...")
print(names)
print()
print("Here is the randomly selected name from the list...")
print()
print("ChoiceNo Name")
print("-------- ----")
# use for loop to repeat this program, three times...
for choiceNo in range(1,4):
    # use choice to select a random name from the list of multiple choices
    name = choice(names)
    # print out the randomly selected name from the array
    print(choiceNo,name)
