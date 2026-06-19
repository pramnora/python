# PROGRAM: [word-dice.py]  

**COMPUTER**: Home based, Nuc MiniPC box      
**OPERATING SYSTEM**: Linux Mint OS, Version 22.3  
**PROGRAMMING LANGUAGE**: Python3, Version: 3.12.3  
**EDITOR**: GNU Nano 7.2  

**AUTHOR**: Mr. Paul Ramnora  
**LOCATION**: London, UK  
**EMAIL**: paulramnoracoder@yahoo.com  

**CREATED**: *Fri 19th June 2026 19:37 PM GMT*  
**UPDATED**: *Fri 19th June 2026 19:37 PM GMT*  

-----

## Explanation  

A simple dice throw program...;  
which prints out the 'dice number' as being a 'word number' instead of an actual number.   

-----

The program, first, imports the library called: random.

> import random  

Random, is a Python 'built-in' library which allows one to do things like:   
- produce random numbers  
- make random choices  
- etc.  

-----

Next, it uses a random method called: randint() to output the simulation of a dice throw: 

## CODE SYNTAX  

random.randint(minNo,maxNo).  

-----

## ACTUAL CODE  

> import random  
> diceNo = random.randint(1,6)  

-----

### CREATE A NUMS[] LIST ARRAY TO STORE EACH DICE NUMBER AS BEING A WORD  

The program creates a list items array called: nums;  
which is used to store each word number ranging from: 
'one' going up to 'six'.

nums=["one","two","three","four","five","six"]

-----

Finally, the program employs a series of 6 x if then statements...;  
each of which is used to select which number word is to be printed out...;        
corresponding with whichever dice number was thrown.  

## ACTUAL CODE  

> if diceNo == 1: print(nums[diceNo-1])  
> if diceNo == 2: print(nums[diceNo-1])  
> if diceNo == 3: print(nums[diceNo-1])  
> if diceNo == 4: print(nums[diceNo-1])  
> if diceNo == 5: print(nums[diceNo-1])  
> if diceNo == 6: print(nums[diceNo-1]  

So, if a 1 was thrown...; the word 'one' would be printed out;  
and, if a 2 was thrown...; then, the word 'two' would be printed out;  
and, so on.  

NOTE: As the array index number starts counting from 0 through to 5;  
therefore, it's necessary to state: [diceNo-1]...to printout the right number word.  

-----

**NOTE(S)**:  

This program is the same as [dice.py]; only the output is being shown in the form of words/as opposed to numbers.    

It would be possible to re-write the 6 x if selection lines to be more 'compact' by changing these into being a loop format:    

> for eachLoopNo in range(1,6+1):  
>     if eachLoopNo == diceNo: print nums[diceNo-1])  

...then, the code would be just 5 lines long, instead.  

> import random  
> print(random.randint(1,6))  
> nums=["one","two","three","four","five","six"]  
> for eachLoopNo in range(1,6+1):    
>     if eachLoopNo == diceNo: print nums[diceNo-1])  

-----

## SCREENSHOT PICTURES  

### PROGRAM: Source code  A (original/for, beginners this version reads a lot more clear)  

![Source code](source-code-word-dice-190626-1928.png "The actual program file source code.")    

### PROGRAM: Source code  B (alternative more 'compact' code version using a for loop to select)        

![Source code](source-code-word-dice-B-190626-2016.png "The actual program file source code(alternative more 'compact' code version).")   

### PROGRAM: Output  

![Output](output-word-dice-190626-1929.png "The actual program file output screen.")  
