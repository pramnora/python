# -----------------------------------------------------
# File created: 15:47 05/12/2020
# Last updated: 15:47 05/12/2020
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
# keyword: map(func, seq)

# Example 1:

listOfNums = [1,2,3,4,5]
times2 = lambda x:x*2
print(list(map(times2,listOfNums)))
# outputs: [2,4,6,8,10]

# Example 2:

print(list(map(lambda x:x*2,[1,2,3,4,5])))
# outputs: [2,4,6,8,10]
