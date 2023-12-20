# -----------------------------------
#  PROGRAM: Question & Answer test...
#  VERSION: 1.0.3
# LANGUAGE: Python 3
#       OS: Linux Mint
# COMPUTER: Home based PC 
# -----------------------------------
# Created: Wed 201223 07:32 AM GMT
# Updated: Wed 201223 22:05 PM GMT
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

q=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
a=["alpha","bravo","charlie","delta","echo","foxtrot","golf","hotel","india","juliet","kilo","lima","mike","november","oscar","papa","quebec","romeo","sierra","tango","uniform","victor","whisky","x-ray","yankee","zulu"]

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
print("Your total score is: ",s, "out of",n,"correct guesses.")
