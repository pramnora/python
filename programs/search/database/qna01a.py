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
# 'qNa/question and answer' example database program.

# It can be very quickly and easily adapted
# to suit many different types of 'question/answer' tests...
# - guess codes: (What is .- ? for Morse code/The answer is: a)
# - guess foreign language words (What is un ? for French/The answer is: one)
# - guess maths sums (What is 5+5 ?/The answer is: 10)  
# - etc.
# ...quite simply, by changing the database of related: 'questions/answers'.

# At any time during the program run...; 
# the user is given the option to Quit by pressing either keys: 'q/Q'

# When the program finishes...; it prints out a user score
# stating exactly how many questions had been guessed either right/wrong:
# "Your total score is: 10 out of 10 correct guesses."

# A LIST OF POSSIBLE FUTURE UPDATES

# At the moment, the questions/answers are executed in strict 'sequential' order...as in questions: 1 up to 10;
# ...but, this order could be changed to become 'randomly' ordered questions, instead.

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

# set variables to track: question counter (n)umber/user's current (g)uess/user's current (s)core...

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
