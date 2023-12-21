#*** QnA/Question and Answer test QUIZ: NATO Phonetic Codes/LANGUAGE: Python3
# (Minimized Version 2: using short/single character variable names)
q=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
a=["alpha","bravo","charlie","delta","echo","foxtrot","golf","hotel","india","juliet","kilo","lima","mike","november","oscar","papa","quebec","romeo","sierra","tango","uniform","victor","whisky","x-ray","yankee","zulu"]
n,s,g=0,0,"" 
for x in q:
    print(n+1,"> What is",x,"?")
    g=input("Enter your guess/('q'=quit): ")
    if (g.lower()=="q"):
        break
    else:
        print("   The answer is:",a[n])
        if g==a[n]: 
           s+=1
        n+=1
        print()
print("-Finished!")
print("Your total score is: ",s, "out of",n,"correct guesses.")
