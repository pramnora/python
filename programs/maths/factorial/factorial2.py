# CREATED: Sun 270425 00:36 AM GMT
# UPDATED: Sun 270425 00:36 AM GMT
# ------------------------------------------
# This code borrowed from...
# https://www.youtube.com/shorts/6ifc8RC4F3A
# ------------------------------------------

def factorial(n):
    if n==0 or n==1: # if n is 0/or, n is 1...
       return 1      # ...then, return 1
    else:            # if n > 1/and, n > 0...then, use loop to calculate result
       result=1
       for i in range(2,n+1): # loop counts from 2 up to 5
           result*=i          # calculate result
       return result          # return result

number=5
result=factorial(number)
print(f"The factorial of {number} is: {result}")
 

# loop run...
# result i result*i
# 1      2 2
# 2      3 6
# 6      4 24
# 24     5 120 
