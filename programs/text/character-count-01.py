#--------------------------------------------------------------
#***  PROGRAM: Character count...
#    LANGUAGE: Python 3.7.1
#    COMPUTER: PC/Windows 10 Pro
#--------------------------------------------------------------
#      AUTHOR: Mr. Paul Ramnora
#       EMAIL: pramnora@yahoo.com
#   COPYRIGHT: (c)2018-, Mr. Paul Ramnora./All rights reserved.
#--------------------------------------------------------------
#     CREATED: TUE 04 DEC 2018 - 20:56 PM GMT
#     UPDATED: TUE 22 JUN 2026 - 18:06 PM GMT
#--------------------------------------------------------------

# variable declarations

alphabetLetters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
numbers="0123456789"
a=e=i=o=u=vowel=consonant=letter=number=other=0

# main program

print("PROGRAM: Vowel count\n")        # print title
print("Please enter a text string:")   # prompt use to enter string
aString=input()                        # get user text input

# do character count

for eachChar in aString:

    if eachChar in vowels:             # check if vowel/or, constant 
        if eachChar == "a": 
           a+=1
           vowel+=1
        if eachChar == "e": 
           e+=1 
           vowel+=1
        if eachChar == "i": 
           i+=1
           vowel+=1
        if eachChar == "o": 
           o+=1
           vowel+=1
        if eachChar == "u": 
           u+=1
           vowel+=1
    else:
        if eachChar.lower() in consonants: consonant+=1

    if eachChar.upper() in alphabetLetters: # check if a letter/or, other
        letter+=1
    else:
      other+=1

    if eachChar in numbers:                 # check if a number
       number+=1
        
# printout characters found

print("-" * 80)
print("Characters: ", len(aString))
print("a","e","i","o","u")
print(a,e,i,o,u)
print("    Vowels: ",vowel)
print("Consonants: ",consonant)
print("   Letters: ",letter)
print("   Numbers: ",number)
print("     Other: ",other,"(Including spaces/punctuation symbols/-etc.)")
