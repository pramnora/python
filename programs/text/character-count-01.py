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
#     UPDATED: TUE 22 JUN 2026 - 21:52 PM GMT
#--------------------------------------------------------------

# COMMENTS

# I've 'updated' this code to include the count of...
# letters: vowels/consonants
# numbers
# other (spaces/punctuation chars/-etc.)
# total characters
# ...but, I'm not at all happy...as I still think it's 'bloatcode'...!
# meaning, it needs 'shortening' down an awful lot.

' --------------------------------------------------------------

# variable declarations

alphabetLetters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
vowels="aeiou"
consonants="bcdfghjklmnpqrstvwxyz"
numbers="0123456789"
a=e=i=o=u=vowel=0
b=c=d=f=g=h=j=k=l=m=n=p=q=r=s=t=v=w=x=y=z=consonant=0
n0=[0]
n1=[0]
n2=[0]
n3=[0]
n4=[0]
n5=[0]
n6=[0]
n7=[0]
n8=[0]
n9=[0]
number=letter=other=0

# function declarations

def doUnderline():
    print("-" * 80)

# main program

print("PROGRAM: Vowel count\n")        # print title
print("Please enter a text string:")   # prompt use to enter string
aString=input()                        # get user text input
# do character count
for eachChar in aString:
    if eachChar in vowels:             # if/else, counts both vowels/consonants
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
        if eachChar.lower() in consonants:
           consonant+=1
        if eachChar.lower() == "b":b+=1
        if eachChar.lower() == "c":c+=1
        if eachChar.lower() == "d":d+=1
        if eachChar.lower() == "f":f+=1
        if eachChar.lower() == "g":g+=1
        if eachChar.lower() == "h":h+=1
        if eachChar.lower() == "j":j+=1
        if eachChar.lower() == "k":k+=1
        if eachChar.lower() == "l":l+=1
        if eachChar.lower() == "m":m+=1
        if eachChar.lower() == "n":n+=1
        if eachChar.lower() == "p":p+=1
        if eachChar.lower() == "q":q+=1
        if eachChar.lower() == "r":r+=1
        if eachChar.lower() == "s":s+=1
        if eachChar.lower() == "t":t+=1
        if eachChar.lower() == "v":v+=1
        if eachChar.lower() == "w":w+=1
        if eachChar.lower() == "x":x+=1
        if eachChar.lower() == "y":y+=1
        if eachChar.lower() == "z":z+=1
    if eachChar.upper() in alphabetLetters: # if/else, counts both letters/othe>
        letter+=1
    elif eachChar not in numbers:
      other+=1
    if eachChar in numbers:                 # if/else, counts numbers
       number+=1
       if eachChar=="0":n0[0]+=1
       if eachChar=="1":n1[0]+=1
       if eachChar=="2":n2[0]+=1
       if eachChar=="3":n3[0]+=1
       if eachChar=="4":n4[0]+=1
       if eachChar=="5":n5[0]+=1
       if eachChar=="6":n6[0]+=1
       if eachChar=="7":n7[0]+=1
       if eachChar=="8":n8[0]+=1
       if eachChar=="9":n9[0]+=1

# printout characters found

doUnderline()
print("Characters: ", len(aString))
print("    Vowels: ",vowel)
print("             a","e","i","o","u")
print("            ",a,e,i,o,u)
print("Consonants: ",consonant)
print("             b c d f g h j k l m n p q r s t v w x y z")
print("            ",b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,w,x,y,z)
print("   Letters: ",letter)
print("   Numbers: ",number)
print("             0   1   2   3   4   5   6   7   8   9")
print("            ",n0,n1,n2,n3,n4,n5,n6,n7,n8,n9)
print("     Other: ",other,"(Including spaces/punctuation symbols/-etc.)")
doUnderline()

            
