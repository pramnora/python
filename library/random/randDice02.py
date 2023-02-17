import random

minNo=1
maxNo=6
noOfDiceThrows=100

for eachDiceThrow in range(1,noOfDiceThrows+1):
    print(eachDiceThrow,": ",random.randint(minNo,maxNo))
    
    
