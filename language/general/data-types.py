# Created: Sun 130425 09:21 AM GMT
# Updated: Sun 130425 09:21 AM GMT
# --------------------------------

# Simple types...

aString1 = "a"
aString2 = 'b'
aChar='A'
aInteger=1
aFloat=1.0
aBoolean=True

# Complex types...

aList=['a',"b",'c',1,2,3]
aTuple=(1,2)
aSet={1,1,2,2} # no duplicates
aDict={'a':1,'b':2,'c':3}

# function...

def aFunc():
    pass

# class...

class aClass:
    pass

# printout

print(aString1,aString2,aChar,type(aString1),type(aString2),type(aChar))
print(aInteger,type(aInteger),aFloat,type(aFloat))
print(aList,type(aList))
print(aTuple,type(aTuple))
print(aSet,type(aSet))
print(aDict,type(aDict))
print(aFunc,type(aFunc))
print(aClass,type(aClass))
