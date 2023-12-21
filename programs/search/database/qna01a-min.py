#*** QnA/Question and Answer test QUIZ: NATO Phonetic Codes/LANGUAGE: Python - (Minimized Version I/using long variable names)
strQuestions=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
strAnswers=["alpha","bravo","charlie","delta","echo","foxtrot","golf","hotel","india","juliet","kilo","lima","mike","november","oscar","papa","quebec","romeo","sierra","tango","uniform","victor","whisky","x-ray","yankee","zulu"]
intCounterNo,intScoreNo,strGuess=0,0,"" 
for strEachQuestion in strQuestions:
    print(intCounterNo+1,"> What is",strEachQuestion,"?")
    strGuess=input("Enter your guess/('q'=quit): ")
    if (strGuess.lower()=="q"):
        break
    else:
        print("   The answer is:",strAnswers[intCounterNo])
        if strGuess==strAnswers[intCounterNo]: 
           intScoreNo+=1
        intCounterNo+=1
        print()
print("-Finished!")
print("Your total score is: ",intScoreNo, "out of",intCounterNo,"correct guesses.")
