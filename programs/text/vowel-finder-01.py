#--------------------------------------------------------------
#***  PROGRAM: Count number of vowels in user entered string...
#    LANGUAGE: Python 3.7.1
#    COMPUTER: PC/Windows 10 Pro
#--------------------------------------------------------------
#      AUTHOR: Mr. Paul Ramnora
#       EMAIL: pramnora@yahoo.com
#   COPYRIGHT: (c)2018-, Mr. Paul Ramnora./All rights reserved.
#--------------------------------------------------------------
#     CREATED: TUE 04 DEC 2018 - 20:56 PM GMT
#     UPDATED: TUE 22 JUN 2026 - 17:18 PM GMT
#--------------------------------------------------------------

#*** BUG LIST FOUND...
#    1. The program only checks to find 'lower case' letters; but, does NOT check to find 'upper case' letters?

aCount=eCount=iCount=oCount=uCount=vowelsCount=consonantsCount=lettersCount=otherCount=0
alphabetLetters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print("PROGRAM: Vowel count\n")
print("Please enter a text string:")
aString=input()
for eachChar in aString:
    if eachChar in vowels:
        if eachChar == "a": 
           aCount+=1
           vowelsCount+=1
        if eachChar == "e": 
           eCount+=1 
           vowelsCount+=1
        if eachChar == "i": 
           iCount+=1
           vowelsCount+=1
        if eachChar == "o": 
           oCount+=1
           vowelsCount+=1
        if eachChar == "u": 
           uCount+=1
           vowelsCount+=1
    else:
        consonantsCount+=1
    if eachChar.upper() in alphabetLetters: 
        lettersCount+=1
    else:
      otherCount+=1
print("a","e","i","o","u")

print(aCount,eCount,iCount,oCount,uCount)
print(len(aString),"characters. (Including spaces/punctuation symbols/-etc.)")
print("   Letters: ",lettersCount)
print("Consonants: ",consonantsCount)
print("    Vowels: ",vowelsCount)
print("     Other: ",otherCount)

