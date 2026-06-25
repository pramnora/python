# This code borrowed from YouTube:
# Python Projects for Beginners (Channel: Bro Code)
# https://www.youtube.com/watch?v=4wGuB3oAKc4&t=3912s
# Project 1: Video position: 0:28-5:45/4:21:31
# ---------------------------------------------------
# NOTE: The code was adopted by me...
#    1. I made the code shorter...using single line if...
#       as opposed to multi-line if/elif.
#    2. I added a while loop to repeat the program.
#    3. I placed the operator check into a single: ("+-*/") 
#    4. I decided to use eval() to cut down multiple if's
#    His code is 20 lines long.../whereas, mine is just 13.
# ---------------------------------------------------
while True:
   operator=input("Enter an operator (+ - * /): ")
   if operator in ("+","-","*","/"):
      num1=input("Enter the 1st number: ")
      num2=input("Enter the 2nd number: ")
      sum=num1+operator+num2
      result=eval(sum)
      print(round(result,2))
   else:
      print("Invalid operator: >" + operator + "<")
      userResponse=input("Want to try, again, Y/N? ")
      if userResponse not in ("Yesyes"):
         break

