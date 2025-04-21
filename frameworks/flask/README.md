# Flask

-----

Created: *Wed 15th Feb 2023 11:51 PM GMT*  
Updated: *Mon 21st Apr 2025 02:35 AM GMT*

-----

## Introduction

Flask, is a Python framework which allows one to very quickly and easily build/test/run web pages.  

-----

## Writing/Testing/Running your 1st Flask app.  

(

>from flask import Flask  
>app = Flask(__name__)  
>@app route('/')  
>def hw():  
>return 'Hello, world! From Flask app'  
>if __name__ == __main__:  
>app.run(debug=True)

Thus, it took no more than merely just 7 lines of code...to go create a Flask app. How totally 'cool' is that...?!  

-----  

**NOTE(S)**: 

1- For some weird reason the above code has not been formatted properly on GitHub web pages...;  
Git Hub is taking out the double underscores(__) that are meant go either side of 'name/main'...;      
so, in that case, I would recommend you look at the file called: hw01.app in the 'test/hw' directory,     
in order to see what the correctly formatted code looks like. Here is the link:    

- https://github.com/pramnora/python/blob/master/frameworks/flask/test/hw/hw01.py  

2- The above code was tested using: PC/Linux Mint OS/Nano editor  

3- If Flask is not already installed...; you can install it by using the command:    
>pip install flask      

4. The above code was borrowed from:
- https://www.geeksforgeeks.org/flask-creating-first-simple-application/  

5. In order to run the above code, use command:  
>Python3 hw01.py  

6. In order to see the code up and working inside of your own web browser...; go to your local host URL address:    
- http://127.0.0.1:5000  
...and, there you should witness seeing the 'output' of your very first 1st Flask web page app.  
Warmest congratulations! ;-)

7. When you wish to shut down the web server...; and, thus, stop the web page output from running...  

>[CTRL]+[C]  

...which will allow you to still continue editing:  
>nano hw01.py        

-----  

## Links

### YouTube videos

Simple Web App with Flask and Heroku - Python GUI for Beginners (Channel: Python Simplified)  
- https://www.youtube.com/watch?v=6plVs_ytIH8  

### Flask site hosting

PythonAnywhere.com  
- https://www.pythonanywhere.com

### Example codes...

Article: Answer to ?: How to create a simple Flask application    
- https://www.geeksforgeeks.org/flask-creating-first-simple-application/  

Article: Digital Ocean: How to Build a Flask Python Web Application from Scratch  
- https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

Article: Digital Ocean: How and When to Use Sqlite  
- https://www.digitalocean.com/community/tutorials/how-and-when-to-use-sqlite  

