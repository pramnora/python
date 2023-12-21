# -----------------------------------
#  PROGRAM: Question & Answer test...
#  VERSION: 1.0.4
# LANGUAGE: Python 3
#       OS: Linux Mint
# COMPUTER: Home based PC 
# -----------------------------------
# Created: Wed 201223 07:32 AM GMT
# Updated: Thu 211223 13:21 PM GMT
# -----------------------------------

# WHAT THE PROGRAM DOES
# This is a very simple 
# 'qna/question and answer' example database...;
# which can very quickly and easily be adapted
# to suit many different types of 'question/answer' tests.

# ------------------------
# Variable declarations...
# ------------------------

# Quiz: NATO Phonetic Alphabet codes 

# First, create 2 parallel arrays...

# q, stores the questions
# a, stores the answers

# Next, inialise the arrays with values...questions/answers...

q=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
a=["alpha","bravo","charlie","delta","echo","foxtrot","golf","hotel","india","juliet","kilo","lima","mike","november","oscar","papa","quebec","romeo","sierra","tango","uniform","victor","whisky","x-ray","yankee","zulu"]

# set variables to track: question number/user's current guess/user's current score...

n=0  # variable stores the current question counter (n)umber
g="" # variable stores the users current (g)uess
s=0  # variable stores what is the users current (s)core

# ---------------
# Main program...
# ---------------

for x in q:
    print(n+1,"> What is",x,"?")
    g=input("Enter your guess/('q'=quit): ")
    if (g.lower()=="q"):
        break
    else:
        print("   The answer is:",a[n])
        if g==a[n]: 
           s+=1
        n+=1
        print()
print("-Finished!")
print("Your total score is: ",s, "out of",n,"correct guesses.")
