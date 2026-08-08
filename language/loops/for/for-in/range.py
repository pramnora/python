for x in range(10):   # the count starts at 0...and, finishes -1 from the loop specified count...eg. 0-9 
    print (x,end=" ") # the end=" " prints horizontally across/with a space showing in between each number 
print()               # reset cursor              
# 0 1 2 3 4 5  6 7 8 9

for x in range(1,10): # this sets the count to start from 1...and, end at 9...= 10 (-1)
    print (x,end=" ") # the end=" " prints horizontally across/with a space showing in between each number 
print()               # reset cursor              
    
#1 2 3 4 5 6 7 8 9

for x in range(1,10,2): # this sets the step of the count...count up in steps of 2 at a time
    print (x,end=" ")   # the end=" " prints horizontally across/with a space showing in between each number 
print()                 # reset cursor              
    
#1 3 5 7 9

for x in range(0,10,2):
	print (x)        # normal print/prints with new line at the end
    
#0
#2
#4
#6
#8 

-----

# Update: 080826 05:06 AM GMT 

for x in range(10,0,-1):
    print (x,end=" ") # the end=" " prints horizontally across/with a space showing in between each number 
print()               # reset cursor              
# 10 9 8 7 6 5 4 3 2 1
