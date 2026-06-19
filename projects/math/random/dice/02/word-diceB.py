import random
diceNo=random.randint(1,6)
nums=["one","two","three","four","five","six"]
for eachLoopNo in range(1,6+1):
    if eachLoopNo == diceNo: print(nums[diceNo-1])
