# ----------------------------------------------
#  Program: Add successive numbers.../Version II
#           This version used a procedure,
#           instead, of a solo for loop
#           to do the counting.
# Language: Python/Version: 3.11.1
#   Editor: IDLE
# ----------------------------------------------
# Computer: Home based/Desktop PC
#       OS: Windows 10 Professional
# ----------------------------------------------
#   Author: Mr. Paul Ramnora
#    Email: pramnora@yahoo.com
# Location: London, UK
# ----------------------------------------------
#  Created: Mon 13th Feb 2023 14:22 PM GMT
#  Updated: Mon 13th Feb 2023 14:22 PM GMT
# ----------------------------------------------

# initialise global variables...

maxNum = 1000000                        # 1 million digits to be added up/
                                        # (1 million = a 1 followed by 6 x 0's : 1,000,000)
                                        
# procedures listing...

def  sumOfNums(maxNum):
     '''
      This program uses a for loop to add up each successive number: 1+2+3,-etc.;
      then, returns back the sum total of all digits added up...
     '''
     
     totalNums=0                         # total starts at 0
    
     for eachNum in range(1,maxNum + 1): # loop variable: eachNum, counts up from 1...up to...maxNum
          totalNums += eachNum           # eachNum is added into the value of totalNums

     return totalNums                    # whenever the for loop has finished running...;
                                         # the program returns back the sum total value of all nums

# main program...

print(sumOfNums(maxNum))                 # make procedure call...passing in the value of maxNum;
                                         # then, print out total

