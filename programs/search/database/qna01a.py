# -----------------------------------
#  PROGRAM: Question & Answer test...
#  VERSION: 1.0.1
# LANGUAGE: Python 3
#       OS: Linux Mint
# COMPUTER: Home based PC 
# -----------------------------------
# Created: Wed 201223 07:32 AM GMT
# Updated: Wed 201223 07:32 AM GMT
# -----------------------------------

# WHAT THE PROGRAM DOES
# This is a very simple 
# 'qna/question and answer' example database...;
# which can very quickly and easily be adapted
# to suit many different types of 'question/answer' tests.

# ------------------------
# Variable declarations...
# ------------------------

# First, create 2 parallel arrays...
# q, stores the questions
# a, stores the answers

q=["a","b","c"]
a=["1","2","3"]

n=0  # variable stores the current answer counter number
g="" # variable stores the users current guess
s=0  # variable stores what is the users current score

# ---------------
# Main program...
# ---------------

for x in q:
    print(n+1,"> What is",x,"?")
    g=input("Enter your guess: ")
    print("   The answer is:",a[n])
    if g==a[n]: 
       s+=1
    n+=1
    print()
print("-Finished!")
print("Your total score is: ",s)
