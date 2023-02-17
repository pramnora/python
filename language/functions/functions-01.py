# -----------------------------------------------
# Demonstrating the use of Python functions...;
# which may be employed in many different ways...

# Created: Fri 17 Feb 2023 08:53 AM GMT
# Updated: Fri 17 Feb 2023 08:53 AM GMT
# -----------------------------------------------


def printMsg1(msgText):
  print("1: ",msgText)

printMsg1("Hello, world!") # call with 1 argument


def printMsg2(msgText="Set a default text message."):
  print("2: ",msgText)
 
printMsg2() # call with no arguments/uses the 'default' already set argument


def printMsg3(msgText):
  print("3: ",msgText)

msg1="concatenating two strings"
msg2="during call"
printMsg3(msg1+msg2) # call with concatenated arguments


def printMsg4(msgText):
  print("4: ",msgText)
  
myList=[1,1+2,"two",{'number':3},True,1==2] # list containing multiple different types of data: 
                                            # number,mathematical expression, string, object, boolean, boolean expression
printMsg4(myList) # call using a list


def retConcat(msgText):
  return("5: ","X"+msgText+"X") # returns a single value passed in/plus, concatentation on both sides of string

print(retConcat("Returned text"))# call using return statement


def retAdd(a,b):
  return("6: ",a+b) # returns back the sum total of 2 values passed in

print(retAdd(1,2)) # call passes in 2 values


def retIncrement(a,b):
  return(a+1,b+1) # returns back 2 values with both incremented

print("7: ",end="") 
x,y=(retIncrement(3,4)) # Call passes in 2 values
print(x,y)
