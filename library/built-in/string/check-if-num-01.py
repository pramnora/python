import string

def checkIfNumber(strNum):
  if strNum in string.digits:
    print("Y")
  else:
    print("N")

checkIfNumber("1")
#Y
checkIfNumber("a")
#N

