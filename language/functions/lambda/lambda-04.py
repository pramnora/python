# Demo: Lambda, how to use 'default' arguments...

# create function

double=lambda y=3:y*2 # setting a 'default' argument

# make function calls

print(double())  # outputs: 6 (2*3)/using function 'default' value
print(double(4)) # outputs: 8 (2*4)/using function call value 
