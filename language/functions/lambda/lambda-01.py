# -----------------------------------------------------
# File created: 14:55 05/12/2020
# Last updated: 14:55 05/12/2020
# -----------------------------------------------------
# Original code borrowed from...
# YouTube: Channel: freeCodeCamp.org 
# Intermediate Python Programming Course
# https://www.youtube.com/watch?v=HGOBQPFzWKo&t=7222s
# video point: 2:00:31/5:55:46
# -----------------------------------------------------
# Original code further adapted by me: 
# (c) 2020-, Mr. Paul Ramnora./All rights reserved.
# -----------------------------------------------------

# SYNTAX Usage
# keyword: lambda + space + variable-name/(or, comma seperated variable names list):expression

# NOTE: a> Lambdas, can be used as a quick way to write simple 1 line functions/
#          as opposed to using multiple lines of code.
#       b> They can also be used as function arguments as well

# Example 1: Mathematical Lambda

addPlus1=lambda num:num+1
print(addPlus1(1))
# outputs: 2

# Example 2: String Lambda

combine2strings=lambda string1,string2:string1+string2
print(combine2strings("Hello, ","world!"))
# outputs: Hello, world!
