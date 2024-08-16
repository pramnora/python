# ---------------------------------------
#  PROGRAM: Maths: Shopping list calulator
# LANGUAGE: Python3
# ---------------------------------------
# COMPUTER: Home based PC
#       OS: Linux Mint
# ---------------------------------------
#   AUTHOR: Mr. Paul Ramnora
#    EMAIL: paulramnoracoder@yahoo.com
# ---------------------------------------
#  CREATED: Fri 16 Aug 2024 16:53 PM GMT
#  UPDATED: Fri 16 Aug 2024 16:53 PM GMT
# ---------------------------------------

# -----------------------------------------------
# NOTE: Originally, I had created this file at...
# - https://onecompiler.com/python/42pc6vx2f
# I merely used 'copy and paste'.

# In fact, I wrote the original source code
# on my own home computer: Linux Mint OS
# using the Julia programming language;
# and, wanted to test out if that same source code
# was likely to work using Python 3? Answer: yes.
# -----------------------------------------------

# variable declarations...
bananas, oranges, tomatoes = 7 * 0.29, 1.50, 1.10     # initialising mutliple variables using just one same line

# array declaration...
araShopping = [bananas, oranges, tomatoes]            # create an array, and, initialise it using variable values

# print out each of the array values...
for eachItem in araShopping:                          # use loop to go through each array value
    print(eachItem)                                   # print out each array value     
    
# calculate and print shopping total value...     
sumTotal = 0                                          # initialise sumTotal variable
for each_item in araShopping:                         # use for loop to go through each array value
    sumTotal += each_item                             # calculate sum total value 
print("====")                                         # print equals line    
print(sumTotal)                                       # printout sum total value   

# ---------------------
# Output...
# 
# 2.03
# 1.5
# 1.1
# ====
# 4.63
