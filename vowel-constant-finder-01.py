#-------------------------------------------------------------------------
#***  PROGRAM: Count number of vowels/consonants in user entered string...
#    LANGUAGE: Python 3.7.1
#    COMPUTER: PC/Windows 10 Pro
#-------------------------------------------------------------------------
#      AUTHOR: Mr. Paul Ramnora
#       EMAIL: pramnora@yahoo.com
#   COPYRIGHT: (c)2018-, Mr. Paul Ramnora./All rights reserved.
#-------------------------------------------------------------------------
#     CREATED: TUE 4 DEC 2018 - 21:24 PM GMT
#     UPDATED: TUE 4 DEC 2018 - 21:24 PM GMT
#-------------------------------------------------------------------------

#*** BUG LIST FOUND...
#    1. This program is, essentially, bloat-code; and, therefore, needs to be considerably slimmed down...!
#    2. The program only checks to find 'lower case' letters; but, does NOT check to find 'upper case' letters?

vowels="aeiou"
aCount=eCount=iCount=oCount=uCount=0

consonants="bcdfghjklmnpqrstvwxyz"
bCount=cCount=dCount=fCount=gCount=hCount=jCount=kCount=lCount=mCount=nCount=oCount=pCount=qCount=rCount=sCount=tCount=uCount=vCount=wCount=xCount=yCount=zCount=0

print("PROGRAM: Vowels/Constants count\n")

aString=input("Please, enter a text string: ")

for eachChar in aString:
    
    if eachChar in vowels:
        if eachChar == "a": aCount+=1
        if eachChar == "e": eCount+=1
        if eachChar == "i": iCount+=1
        if eachChar == "o": oCount+=1
        if eachChar == "u": uCount+=1
        
    if eachChar in consonants:
        if eachChar == "b": bCount+=1
        if eachChar == "c": cCount+=1
        if eachChar == "d": dCount+=1
        if eachChar == "f": fCount+=1
        if eachChar == "g": gCount+=1        
        if eachChar == "h": hCount+=1
        if eachChar == "j": jCount+=1
        if eachChar == "k": kCount+=1
        if eachChar == "l": lCount+=1
        if eachChar == "m": mCount+=1
        if eachChar == "n": nCount+=1
        if eachChar == "p": pCount+=1
        if eachChar == "q": qCount+=1
        if eachChar == "r": rCount+=1
        if eachChar == "s": sCount+=1
        if eachChar == "t": tCount+=1
        if eachChar == "v": vCount+=1
        if eachChar == "w": wCount+=1
        if eachChar == "x": xCount+=1        
        if eachChar == "y": yCount+=1
        if eachChar == "z": zCount+=1

print(len(aString),"characters")

print("a","e","i","o","u")
print(aCount,eCount,iCount,oCount,uCount)

print("b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","y","z")
print(bCount,cCount,dCount,fCount,gCount,hCount,jCount,kCount,lCount,mCount,nCount,pCount,qCount,rCount,sCount,tCount,vCount,wCount,xCount,yCount,zCount)
