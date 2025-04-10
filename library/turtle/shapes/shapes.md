CREATED: Thu 10th April 2025 13:36 PM GMT  
UPDATED: Thu 10th April 2025 13:36 PM GMT  

Explaining how the: [shapes.py] program was developed/created...

-----

PROGRAM: FIRST DRAFT

At first, I started with the following code...;   
which uses a combination of LOGO Turtle graphics(Python library)/   
and, Python programming language 'for' loop code...     
to draw a simple 4 sided square onto the output screen.    

>>import turtle  
>>for drawSquare in range(1,5):  
>>    turtle.forward(100)  
>>    turtle.left(90)

-----

PROGRAM: SECOND DRAFT

Next, I decided to change the above code into becoming   
a 'self-contained' function call;    
with the function having 'a specific shape name': drawSquare().   
  
Because it was a function call...  
rather than 'hard code' the function...each time;  
meaning, having to enter into the function itself to change number;      
I decided to call it by passing in 3 variable arguments, namely:      
length/degrees/totalSides.  

>>import turtle  
>>def drawSquare(length,degrees,totalSides):       
>>noOfSides=totalSides  
>>for drawSquare in range(1,noOfSides+1):  
>>    turtle.forward(length)  
>>    turtle.left(degrees)  
>>
>>drawSquare(100,90,4)     # draws a Square shape  

-----

PROGRAM: THIRD DRAFT

In my 3rd program iteration,  
I decided to create 2 entirely different shapes...;    
by using the same function code above...  
(just use 'copy and paste'/then, 'rename' the function);    
the first function call would draw a triangle: drawTriangle();      
the second function call would draw a square: drawSquare();    
with each function call being made separately.    

>>import turtle  
>>    
>>def drawTriangle(length,degrees,totalSides):     
>>noOfSides=totalSides  
>>for drawTriangle in range(1,noOfSides+1):  
>>    turtle.forward(length)  
>>    turtle.left(degrees)  
>>
>>def drawSquare(length,degrees,totalSides):       
>>noOfSides=totalSides  
>>for drawSquare in range(1,noOfSides+1):  
>>    turtle.forward(length)  
>>    turtle.left(degrees)  
>>  
>>drawTriangle(100,120,3)  # draws a Triangle shape  
>>drawSquare(100,90,4)     # draws a Square shape  

-----

PROGRAM: FORTH DRAFT

Then, of course, I realised that all of the shape arguments: length/degrees/totalSides...;    
had already been 'pre-declared'...; and, these could, in fact, be used to draw 'any' shape;    
meaning, I only have to make just 'one' function call...; and, delete all the rest of them;    
so, I decided to rename the function as being called, more generically, drawShape().      

>>import turtle
>>    
>>def drawShape(length,degrees,totalSides):         
>>noOfSides=totalSides  
>>for drawShape in range(1,noOfSides+1):    
>>    turtle.forward(length)    
>>    turtle.left(degrees)  
>>
>>drawShape(100,120,3)  # draws a Triangle shape  
>>drawShape(100,90,4)   # draws a Square shape  

-(**PROGRAMMING TIP**: **DRY** - *D*on't *R*epeat *Y*ourself.)-  

-----

PROGRAM: FIFTH DRAFT

In my next iteration...I decided to *optimize* the code...;     
which I thought was just a bit too long.  

For this step, I made 2 changes...  

Change number 1: Make the code more compact...  

>>noOfSides=totalSides  
..wasn't necessary. I could delete that line; by placing 'noOfSides' in the function call parameter list:   
>>def drawShape(length,degrees,noOfSides):         

Change number 2: Get rid of the 'degrees' variable...;   
and, let the program itself calculate the number of degrees to use(360/noOfSides):

eg. 360/3 = 120 (120+120+120=360) # draw a triangle/(3 sides)     
eg. 360/4 = 90 (90+90+90+90=360)  # draw a square/(4 sides)  
eg. 360/5 = 72 (72+72+72+72+72=360) # draw a pentagon shape/(5 sides)  
-etc.  

So, the function parameter list was now shortened by getting rid of 1 unnecessary argument to become  
instead of 3 arguments to pass in...just, simply, 2:       
>>def drawShape(length,noOfSides):           

The 'shortened' code, now looked like this...;  
and, just to test that it worked...I decided to add another function call:   
draw a pentagon shape with 5 sides.  

>>import turtle  
>>    
>>def drawShape(length,noOfSides):         
>>for drawShape in range(1,noOfSides+1):    
>>    turtle.forward(length)    
>>    turtle.left(360/noOfSides)  
>>
>>drawShape(100,3)  # draws a Triangle shape/(3 sides)   
>>drawShape(100,4)   # draws a Square shape/(4 sides)  
>>drawShape(100,5)   # draws a Pentagon shape/(5 sides)  

Luckily, it all worked, succcessfully.

-----

CONCLUSION

The only difficulty I'm having, at the moment, is...;  
the output screen appears only for a short while...just merely 1 or 2 seconds;   
then, completely disappears...;  
so, I cannot get the 'enjoy' seeing the program output for too very long...?!  
I will try and Google how to fix this...???

I found the answer to the above question inside of this 'stackoverflow' article:    

- https://stackoverflow.com/questions/19018243/python-turtle-graphics-window-only-opens-briefly-then-closes        

Basically, the article states...in order to stop the output window from disappearing...  
you can either use the line...
  
>>turtle.done()    

...or,...  

>>turtle.mainloop()  

...I tried it...and, yes, it works. Eureka! LOL Happy days...!!!  
Now, I can stop all of my graphical turtle output from, all of sudden, completely disappearing.  


 
