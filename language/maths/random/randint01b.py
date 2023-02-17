# import libraries

import random

# initialise global variables

minDiceNo=1
maxDiceNo=6
noOfDiceThrows=100

# main program

for eachDiceThrow in range(1,noOfDiceThrows+1):
    print("Dice throw:(",eachDiceThrow,")",random.randint(minDiceNo,maxDiceNo))
