CREATED: Thu 10th April 2025 13:36 PM GMT  
UPDATED: Thu 10th April 2025 13:36 PM GMT  

-----

PROGRAM: FIRST DRAFT

At first, I started with the following code...;   
which uses a combination of LOGO Turtle graphics(Python library)/  
and, Python 'for' loop to draw a simple 4 sided square onto the output screen.  

>>import turtle  
>>for drawSquare in range(1,5):  
>>    turtle.forward(100)  
>>    turtle.left(90)

-----

PROGRAM: SECOND DRAFT

Next, I decided to change the above code into becoming   
a self-contained function call;    
with the function having 'a specific shape name';  
because it was a function call...  
I decided to call it by passing in a number of variable arguments, namely:    
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
the first function call would draw a triangle;    
the second function call would draw a square;  
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

-(**PROGRAMMING TIP**: **DRY** - *D*o NOT *R*epeat *Y*ourself.)-  

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

-----

PROGRAM: FORTH DRAFT


 
