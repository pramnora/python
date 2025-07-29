# Demo: How to use anonymous lambda...

# create anonymous function

def myfunc(n):
    return lambda a:a*n

# initialise a

mydoubler=myfunc(2)
mytripler=myfunc(3)

# initialise n

print(mydoubler(2)) # outputs: 4
print(mytripler(2)) # outputs: 6
