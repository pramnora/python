# PROGRAM: Hello, world!/(5 different methods of writing the code...)
# LANGUAGE: Python 2
# SITE: https://trinket.io
# CREATED: Wed 3rd Nov 2021 11:12 AM GMT
# UPDATED: Wed 3rd Nov 2021 11:12 AM GMT

# Demo: How to output text 5 different ways using Python 2...

# print a string literal...

print "Hello, world!(1)"

# print a string variable...

strMessage = "Hello, world!(2)"
print strMessage

# using a function to print a string variable...

def printMessage(strMsgText):
  print strMsgText
  
printMessage("Hello, world!(3)")

# using a function to return a 2 concatenated -(joined together using the + symbol)- string variables...

def printMessage2(strTextMsg1,strTextMsg2):
  return strTextMsg1 + strTextMsg2
  
print printMessage2("Hello, ","world!(4)")  

# print string literal text using the 'new line' symbol: \n... 

print "Hello,\nworld!(5)"
  
