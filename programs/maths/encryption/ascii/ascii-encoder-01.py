# File created: Wed 14 Aug 2024 17:21 PM GMT 
# Last updated: Wed 14 Aug 2024 17:21 PM GMT
# ------------------------------------------
# This is the start of an encoding program...
# It tranlates a plain text alphabet message: A-Z;
# into becoming a series of alphabet numbers: 1-26.
# ------------------------------------------

# initialise variable...
secret_message="This is a secret message."

# shorten variable name/plus, change each letter to become upper case...
sm=secret_message.upper()

for eachChar in sm:                         # loop through each character in secret message...
    if eachChar >= "A" and eachChar <= "Z": # check character is: A-Z 
        n = ord(eachChar)-64                # get letter ASCII number: 65-90/deduct 64: (1-26)
        if n < 10:                          # if ASCII number is less than 10/(if number is a single digit)
            n  = '0' + (str(n))             # add a 0 prefix digit to that number
        print(n,end="")                     # print numbers all on one single same line/with no spaces in between
 
print("\n")                                 # vertical line break/ceases all output to one same line

# -----------------------------------------------------------------------
# The secret message gets translated into being a series of number pairs:   
# 20 08 09 19 = T H I S/-etc.  
# 
# 2008091909190119050318052013051919010705  
