# CREATED: Mon 230625 00:48 AM GMT
# UPDATED: Mon 230625 00:48 AM GMT
# --------------------------------
# Here the letters of the alphabet are reversed...
# in order to do a substitution cyper...eg( A=Z/Z=A)

# A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
# Z Y X W V U T S R Q P O N M L K J I H G F E D C B A

# NOTE: The formula to calculate how each letter gets translated is:
#       the absolute value of (abs(n-(26+1))/or, abs(n(-27))

msg="Thisisasecretmessage" # message to be encoded
msg=msg.upper()            # convert message into being all UPPER CASE letters

def printAlphabetGoingForwards():
	for n in range(1,27):
		print(chr(n+64),end=" ")
	print()

def printAlphabetReversed():
	for n in range(26,0,-1):
		print(chr(n+64),end=" ")
	print()

def doEncoding(letter):
	letterNo = ord(letter)-64 
	result=abs(letterNo-(26+1))
	print(chr(result+64),end="")

def printMsg():
	for eachLetter in msg:
		print(eachLetter,end="")
	print()

def printMsgEncoded():
	for eachLetter in msg:
		doEncoding(eachLetter)
	print()

print("Encoding method: Alphabet reversed: (A-Z/Z-A)")
print('Formula: abs(n-(26+1))/or, abs(n-27)')
print()
printAlphabetGoingForwards()
printAlphabetReversed()
print()
printMsg()
printMsgEncoded()
