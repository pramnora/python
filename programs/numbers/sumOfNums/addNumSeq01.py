# PROGRAM: Add number sequence; then, output total...

# set global variable values...

minNo=0
maxNo=0
total=0

# main program...

# user instructions...

print("Program: Add up a given number sequence; then, output the total")
print()
print("This program gives the sum total of the number sequence entered.")
print("For example:-")
print("Min no: 1")
print("Max no: 3")
print(" Total: 6/(or, 1+2+3=6)")
print("-----------------------------------------------------------------")

# get user input...

minNo=int(input("Enter min no: ")) 
maxNo=int(input("Enter max no: ")) 

# use loop to calculate total...

for x in range(minNo,maxNo+1):
    total+=x

# print total...

print("Total: ",total)
