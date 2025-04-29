# first, import Flask...  

from flask import Flask  

# Next, create a variable app...that links to the Flask app.  

app = Flask(__name__)  

# Now, set a home page route...  

@app.route('/')  

# Create a function that returns a certain value...to be written to the output web page...  

def hw():  
    return 'Hello, world! From Flask app'  

# Finally call the app to run...;  
# and, also, set: debug=True...so, that one can get to read any error output messages...  

if __name__ == '__main__':
    app.run(debug=True)


# --------------------
# Some further notes:- 
# --------------------

'''
The above code was 'tested' to work on: PC/Linux Mint OS/Nano editor.

RUN THE PYTHON FILE: [filename.py]  
In order to run the above...in the Linux terminal type:  
>Python3 hw01.py

VIEW THE OUTPUT IN YOUR WEB BROWSER  
In order to view the code output inside of your 'default' web browser software:  
- http://127.0.0.1:5000  

HOW TO STOP THE WEB SERVER RUNNING  
[CTRL]+[C], shuts down the web server...so, that you can continuing editing.
'''
