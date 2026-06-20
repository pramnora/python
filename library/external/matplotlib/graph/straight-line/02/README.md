# Matplotlib

**CREATED:**: *Sat 20 Jun 2026 03:02 PM GMT*  
**UPDATED:**: *Sat 20 Jun 2026 03:02 PM GMT* 

-----

## Introduction

Speaking as a 'beginner'...I find Matplotlib fairly straight forwards, and, simple to use...;    
one uses it to plot many different styles of graphs, including:  

- straight line     
- bar chart    
- scatter plot  

-----

In this particular example...the code starts off by  
importing the matplotlib library: import matplotlib  
and, calling one of it's related methods: pyplot  
and, also, using a short form alias: plt    
-(in this way, we don't need to keep typing in the long form: matplotlib.pyplot;     
  and, can just type in short form prefix; plt)-  

> import matplotlib.pyplot as plt  

-----

The next part of the code sets up co-ordinates representing both the (x,y) chart axis;        
where x is the horizontal bottommost axis extending going across from left to right;    
and, y is the vertical axis extending going upwards from top to bottom.    

> x = [5,10,15,20,11,12,14,6,18,25,2,8]  
> y = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]    

What this means is the horizontal x axis will display the months going across;    
and, the vertical y axis will display the numbers going upwards.  

-----

The next step is to plot the chart using:   

> plt.plot(x,y)  
...only, the chart itself will NOT show. To do that you need to add the following line...    
> plt.show()  

...and, that's it code done.  

-----

To run the program inside of Linux Minu OS Terminal application command window, type:  

> python graph01A.py  

...and, a window will open up displaying the chart as follows.  

![straight-line-chart-01](graph01A.py "This is the chart showing horizontal straight lines.")  
