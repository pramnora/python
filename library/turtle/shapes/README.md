CREATED: Thu 10th April 2025 13:36 PM GMT  
UPDATED: Thu 10th April 2025 13:36 PM GMT  

-----

PROGRAM: FIRST DRAFT

At first, I started with the following code...; which draws a simple 4 sided square.
>>import turtle  
>>for drawSquare in range(1,5):  
>>    turtle.forward(100)  
>>    turtle.left(90)

-----

PROGRAM: SECOND DRAFT

Next, I decided to change the above code into being a function call, instead;
with the function having a specific shape name.

>>def drawTriangle(length,degrees,totalSides):   
>>import turtle  
>>noOfSides=totalSides  
>>for drawSquare in range(1,noOfSides+1):  
>>    turtle.forward(length)  
>>    turtle.left(degrees)  
>>
>>drawTriangle(100,90,4)  # draws a Square shape

