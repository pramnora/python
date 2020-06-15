#--------------------------------------------------------------
#***  PROGRAM: Count number of vowels in user entered string...
#    LANGUAGE: Python 3.7.1
#    COMPUTER: PC/Windows 10 Pro
#--------------------------------------------------------------
#      AUTHOR: Mr. Paul Ramnora
#       EMAIL: pramnora@yahoo.com
#   COPYRIGHT: (c)2018-, Mr. Paul Ramnora./All rights reserved.
#--------------------------------------------------------------
#     CREATED: TUE 4 DEC 2018 - 20:56 PM GMT
#     UPDATED: TUE 4 DEC 2018 - 20:56 PM GMT
#--------------------------------------------------------------

#*** BUG LIST FOUND...
#    1. The program only checks to find 'lower case' letters; but, does NOT check to find 'upper case' letters?

vowels="aeiou"
aCount=eCount=iCount=oCount=uCount=0
print("PROGRAM: Vowel count\n")
aString=input("Please, enter a text string: ")
for eachChar in aString:
    if eachChar in vowels:
        if eachChar == "a": aCount+=1
        if eachChar == "e": eCount+=1
        if eachChar == "i": iCount+=1
        if eachChar == "o": oCount+=1
        if eachChar == "u": uCount+=1

print(len(aString),"characters")
print("a","e","i","o","u")
print(aCount,eCount,iCount,oCount,uCount)
