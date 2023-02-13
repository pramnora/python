# ----------------------------------------
#  Program: Add successive numbers...
# Language: Python/Version: 3.11.1
#   Editor: IDLE
# ----------------------------------------
# Computer: Home based/Desktop PC
#       OS: Windows 10 Professional
# ----------------------------------------
#   Author: Mr. Paul Ramnora
#    Email: pramnora@yahoo.com
# Location: London, UK
# ----------------------------------------
#  Created: Mon 13th Feb 2023 14:02 PM GMT
#  Updated: Mon 13th Feb 2023 14:02 PM GMT
# ----------------------------------------

# This program uses a for loop to add up each successive number
# going from 1...up to...1 million/(1,000,000).

totalNums=0      # total starts at 0 
maxNum=1000000   # 1 million digits to be added up/
                 # (1 million = a 1 followed by 6 x 0's)

for eachNum in range(1,maxNum+1):
    totalNums += eachNum

print(totalNums) # answer: 500000500000
