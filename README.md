# python

PYTHON PROGRAM CODE

Here you will find snippets of Python 3 programming code; which you are freely able to study/learn from. 

Document last updated: *Wed 14th Aug 2024 -08:37 PM GMT*

-----

INTRODUCTION

Python is a FREE programming language. It comes in 2 different versions:

1> Older version: Python 2.X

Print "Hello, world!"

2> Newer version: Python 3.X

Print ("Hello, world!")

**NOTE**: It is highly recommended that you download the 'latest' version of the Python programming language which is Python: 3.x.

(Older versions of the programming language such as Python 2.x are still available to download and use with older legacy code.)

It is possible to have multiple different versions of Python installed; all up and running on the same one computer.

-----

SOME OF THE ADVANTAGES OF LEARNING PYTHON PROGRAMMING

Python is FREE...if you have a computer internet connection...then, the downloading process is very quick, simple and easy to set up. (It is cross platform: Windows/Linux/Mac/-etc.)  

Python is a very highly popular programming language; therefore, there is much code you can read/study...as well as, tons of tutorial resources...in the form of books/videos/-etc.

Python uses a fairly simple and straight forwards syntax, which makes it really excellent for people who are complete 'beginners' new to programming to learn.

It also includes many advanced features, as well...such as, linking to extended libraries one can use...this make it equally appealing for more experienced: intermediate/and, even, professional programmers.

-----

HOW TO DOWNLOAD PYTHON

To download Python -latest version- go to...

https://www.python.org/downloads/

...and, there click on the Download link.

FIND OUT WHICH VERSION OF PYTHON YOU ARE RUNNING ON WINDOWS OPERATING SYSTEM 

To check which particular version you are using on Windows open up a black screen DOS prompt window; and, type...

C:\> python --version    
...Alternative syntax...  
C:\> python -V  
...Alternative sytax...  
C:\> py -3 --version

PYTHON 3.11.4  

-----

HOW TO SEARCH FOR HELP WITHIN PYTHON ITSELF

C:\> python  
>>> help()  
help> modules  
help> keywords  
help> symbols  
help> topics  

-----

iPython (run Python with line numbers/syntax colour highlighting/-etc.)  

Open up a Black DOS command prompt window...; and, now, type...  

C:\Windows\user>ipython  
...iPython should load, and, display as...   
>>ln [1]: print("Hello, world!")  
>>Hello, world!  
>>  
>>ln [2]:  
>>  

-----

CHECK IF PIP IS INSTALLED/(Python Package Manager)  

Type into the Windows 10 taskbar search box:  
CMD  
Then, when the Command Prompt icon appears...;  
do a 'right click'...and, select:  
Run as Administrator  
Now, a 'black screen' Command Prompt window will appear ready to type further instructions into...    
Type in...  
C:\>pip  
...this should show you a list of PIP command/options...which means, congratulations, you already have PIP installed.    
But, if not...; then use the following command...  
C:\>install pip  

You can also check which version of pip is installed by doing the following...  

C:\WINDOWS\system32>pip --version  
...alternative syntax...
C:\WINDOWS\system32>pip -V    

pip 19.2.3 from c:\users\customer1\appdata\local\programs\python\python38-32\lib\site-packages\pip (python 3.8)  

**NOTE**: If you have Python 3.4 or above...; then, PIP is installed by default.  

UPDATE PIP

C:\>python -m pip install --upgrade pip

C:\Users\customer1>pip --version
pip 20.1 from c:\users\customer1\appdata\local\programs\python\python38-32\lib\site-packages\pip (python 3.8)

UPGRADE PIP ON LINUX MINT OS  

$ python3 -m pip install --upgrade pip   

-----

HOW TO FIND FURTHER PIP COMMANDS

C:\>pip  
...alternative syntax...  
C:\>pip --help  

HOW TO CHECK WHICH SOFTWARE PACKAGES PIP HAS ALREADY INSTALLED

C:\>pip list

HOW TO USE PIP TO INSTALL FURTHER PYTHON SOFTWARE PACKAGES

C:\>pip install numpy

-----

HOW TO USE NUMPY INSIDE OF IDLE

>>>import numpy as np  
>>>xArrayName=np.arange(start=1,stop=10)  
>>>xArrayName  
>>>array([1, 2, 3, 4, 5, 6, 7, 8, 9])  
>>>xArrayName.reshape(3,3)  
>>>array[[1, 2, 3],  
         [4, 5, 6],  
         [7, 8, 9]])  

-----

CHECK IF TKINTER IS INSTALLED

TKInter, allows one to add a GUI/Graphical User Interface to Python programs...(eg, include Windows/Labels/Buttons/-etc.)  

C:\> python -m tkinter  

...a window should appear showing you which version of TKInter is installed;   
the window also contains 2 buttons: Click Me/QUIT  
(click Quit to close the window down)

-----

PYTHON TURTLE GRAPHICS

>>import turtle  
>>for drawSquare in range(1,5):  
>>	turtle.forward(100)  
>>	turtle.left(90)   
>>       turtle.done() # holds the window open so that users can view the output/click window [x] to close.   

-----

Python String library

>>import string  
>>def checkIfNumber(strNum):  
>>    if strNum in string.digits:  
>>        print("Y")  
>>    else:  
>>        print("N")  
>>
>> checkIfNumber("1")  
>> Y  
>> checkIf Number("a")  
>> N  
>>  
         
-----

Python Math library

>>from math import *  
>>for x in range(1,13):  
>>   print(x,"=",math.factorial(x))  
>>  
>>math.pi  
>>3.141592653589793  

-----

Python Time library  

>>import time  
>>print(time.ctime())  
>>Fri May 31 22:46:18 2024  

-----

VPython 3D library

First, you have to install the VPython library; so, at the windows command line type...  

>> pip install vpython  

Now, inside of IDLE type...  

>>from vpython import *   
>>cylinder()  
>>  

...a 3D cylinder shape should appear inside of your 'default' web browser;    
the which 3D shape you can then manipulate by clicking on it using your mouse 'right' button;    
thus, allowing you drag the 3D shape around however you please.  

-----

Pypi/Python Package Index

https://pypi.org/

>>>quote...
Find, install and publish Python packages with the Python Package Index

The Python Package Index (PyPI) is a repository of software for the Python programming language.

PyPI helps you find and install software developed and shared by the Python community. Learn about installing packages.

Package authors use PyPI to distribute their software. Learn how to package your Python code for PyPI.
<<<

-----

CREATE A VIRTUAL ENVIROMENT (.venv)  

I was watching the 'beginners' YouTube tutorial:  

**How to Create a Web Application in Python using Flask**  
- https://www.youtube.com/watch?v=jQjjqEjZK58  


-(NOTE: These instuctions are for Linux Mint OS.)-

I tried typing in...

> python3 -m venv .venv

But, the message said I need to use the following code...

> apt install python3.10-venv

Then, I tried typing in, again...

> python3 -m venv .venv  
> source .venv/bin/activate  

...then, my prompt became this...  

> (.venv) username@hostname:~$  

-----

ADD A DATABASE/(SQLite)

Importing a database library can be achieved by writing just 1 line of code:  

> import sqlite3   

Connecting to the database can be achieved by writing just 1 line of code:   

> conn = sqlite3.connect('anyName.db')

Closing the database can be achieved by writing just 1 line of code:  

> conn.close()

What is more complex to achieve, however, is being able to determine...  
- how many fields to add  
- what sort of data to add into each field  
- how you wish to query the database  
- what fields data you wish to see printed out   
...however, my repository does give some examples.  

-----
  
## LINKS

### DOWNLOAD  

### Language

- https://www.python.org/  
- https://www.python.org/downloads/
- https://pypi.org/

### IDE/Integrated Development Environment

Anaconda   
- https://www.continuum.io/downloads  

JUPYTER  
- http://www.jupyter.org  
- https://jupyter.org/try  
- https://jupyter.org/install.html    

Programiz.com
- https://www.programiz.com/python-programming/online-compiler

PythonAnywhere  
- https://www.pythonanywhere.com  

PyTwiddle.com  
- https://pytwiddle.com  
  
## TUTORIALS/INTERACTIVE ONLINE  

- http://www.learnpython.org/   
- http://www.pythonlearn.com  
- http://www.pythontutor.com
- https://www.learnpython.org  
- https://app.datacamp.com/  
- https://www.datacamp.com/tutorial

FREE online eBook: Digital Ocean: How to code in Python3    
- https://www.digitalocean.com/community/books/digitalocean-ebook-how-to-code-in-python  

Neetcode.io  
- https://neetcode.io/problems/python-hello-world   

PEP 8 -- Style Guide for Python Code  
- https://www.python.org/dev/peps/pep-0008/   

Eduonix: The Developer's Guide to Python 3 Programming  
- https://www.eduonix.com/new_dashboard/the-developers-guide-to-python-3-programming  

## YouTube Videos...

Python Tutorial - Python for Beginners - Learn Python Programming [2020]/(YouTube Channel: Programming With Mosh)
- https://www.youtube.com/watch?v=_uQrJ0TkZlc

Python Tutorial for Programmers - Python Crash Course/(YouTube Channel: Programming With Mosh)
- https://www.youtube.com/watch?v=f79MRyMsjrQ&t=2953s

The Complete Python Course For Beginners/(YouTube Channel: Tech With Tim)  
- https://www.youtube.com/watch?v=sxTmJE4k0ho  

Python Tutorial for Absolute Beginners #1 - What Are Variables?  (series: 16 videos/YouTube Channel: CS Dojo)  
- https://www.youtube.com/watch?v=Z1Yd7upQsXY&list=PLBZBJbE_rGRWeh5mIBhD-hhDwSEDxogDg    

Learn Python with Socratica || Python Tutorial || Python Programming  (YouTube Channel: Socratica)  
- https://www.youtube.com/watch?v=bY6m6_IIN94&list=PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-  

## Full length courses

Python for Everybody - Full Course with Dr. Chuck  (YouTube Channel: freeCodeCamp.org)  
- https://www.youtube.com/watch?v=8DvywoWv6fI&t=3398s    

### Python Language: Concepts

Python Classes and Objects || Python Tutorial || Learn Python Programming  (YouTube Channel: Socratica)  
- https://www.youtube.com/watch?v=apACNr7DC_s  

## Python Library Tutorials...

### NumPy

Introduction to Numerical Computing with NumPy | SciPy 2019 Tutorial | Alex Chabot-Leclerc  
- https://www.youtube.com/watch?v=ZB7BZMhfPgk  

Data Analysis with Python - Full Course for Beginners (Numpy, Pandas, Matplotlib, Seaborn)  
- https://www.youtube.com/watch?v=r-uOLxNrNk8  

### TKInter

Tkinter Course - Create Graphic User Interfaces in Python Tutorial/YouTube Channel: freeCodeCamp.org    
- https://www.youtube.com/watch?v=YXPyB4XeYLA&t=640s  

### VPython 

(9 year old teaching.../VPython: Python 3D graphics)   
- https://www.youtube.com/watch?v=jDDNpDZnFAw&feature=youtu.be&fbclid=IwAR1LtqLBaNI-eDyThp4UIxHpPsvsDzoOazMt_scgoqDIxMm1FeXv7sEePpU  

### Other

How to Learn Python Tutorial - Easy & simple! Learn How to Learn Python!  
- https://www.youtube.com/watch?v=5mJ_Qftw2_0

The Python Programming Deception?  
- https://www.youtube.com/watch?v=FeYljNZHjZQ

What Does It Take To Be An Expert At Python?  
- https://www.youtube.com/watch?v=7lmCu8wz8ro  

6 Python Exercise Problems for Beginners - from CodingBat (Python Tutorial #14/YouTube Channel: CS Dojo)  
- https://www.youtube.com/watch?v=lx7oqZ7Nl3k  

### Tips

What Are Python Asterisk and Slash Special Parameters For?  
- https://realpython.com/python-asterisk-and-slash-special-parameters/   

11 Beginner Tips for Learning Python  
- https://realpython.com/python-beginner-tips/  

10 Python Shortcuts You Need To Know (channel: TechWithTim)   
- https://www.youtube.com/watch?v=CssrFJGH_dU

How to learn Python FAST with ChatGPT and Bard? (Channel: Sundas Khalid)  
- https://www.youtube.com/watch?v=xr68cbOxvBs  



### Regular Expressions

Regular Expressions in Python - (Channel: NeuralNine)  
- https://www.youtube.com/watch?v=wnuBwl2ekmo  

Python Tutorial: re Module - How to Write and Match Regular Expressions (Regex) -(Channel: Corey Schafer)  
- https://www.youtube.com/watch?v=K8L6KVGG-7o  

### Sockets

File Transfer via Sockets in Python - (Channel: NeuralNine)  
- https://www.youtube.com/watch?v=qFVoMo6OMsQ  

### PIP

Upgrading PIP: How to Upgrade PIP in Windows by Few Steps - (Channel: Few Steps)  
- https://www.youtube.com/watch?v=VhOhojy0b28  

### Virtual Environments

The Complete Guide to Python Virtual Environments! - (Channel: teclado)  
- https://www.youtube.com/watch?v=KxvKCSwlUv8  


### Web Scraping

Python Tutorial: Web Scraping with BeautifulSoup and Requests - (Channel: Corey Schafer)  
- https://www.youtube.com/watch?v=ng2o98k983k  

Python Web scraping to CSV file| BeautifulSoup | Real Estate Website Scraping - (Channel: Pythonology)  
- https://www.youtube.com/watch?v=RvCBzhhydNk  

Beautiful Soup 4 Tutorial #1 - Web Scraping With Python  - (Channel: Tech With Tim)  
- https://www.youtube.com/watch?v=gRLHr664tXA  

Beautiful Soup 4 Tutorial #2 - Searching and Filtering - (Channel: Tech With Tim)  
- https://www.youtube.com/watch?v=lOzyQgv71_4  

BeautifulSoup find() and find_all() methods - (Channel: Programming Basics)  
- https://www.youtube.com/watch?v=Fin_f2uqmK4  

Using BeautifulSoup and Python to navigate an HTML parse tree - (Channel: Programming Basics)  
- https://www.youtube.com/watch?v=GWXpWU3d23M  


### Other tutorials (non YouTube)  

Course: PythonIsEasy  
- https://www.pirple.com    
CodeExampler.com  
- https://codeexampler.com/python-variables  

## FREE Udemy course...

3 Python projects for beginners/Teacher: Kostadin Ristovski  
(Word cloud/Web scraping links/Google translate text)  
- https://www.udemy.com/course/3-python-projects-for-beginners/?fbclid=%5B%27IwAR1wPCiNkv8tw4ukWjPRxhWQduc7DVXOUzAyetkUBK_wLENmZzvzJEMzFZQ%27%5D  

## PRACTICE ONLINE INSIDE OF WEB BROWSER

- https://codeexampler.com/compiler/python  
- http://www.codesandbox.io  
- http://www.pythonfiddle.com      
- http://www.repl.it  
- https://rextester.com/l/python3_online_compiler      
- http://www.trinket.io    
- https://www.pythonanywhere.com  

## FRAMEWORKS

- https://www.web2py.com  

## BOOKS

- https://books.trinket.io/pfe/

## CODE

- http://www.py4inf.com/code/  
- https://www.py4e.com/code3/  


### Python Certification

- https://openedg.org/  
- https://openedg.org/python-institute  
- https://pythoninstitute.org/  
- https://pythoninstitute.org/pcep  (Certified Entry-Level Python Programmer)  
- https://pythoninstitute.org/pcap  (Certified Associate Python Programmer)  
- https://www.youtube.com/@openedgpythoninstitute  (YouTube channel: OpenEDG Python Institute)  


