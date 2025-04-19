# first, import Flask...  

from flask import Flask  

# Next, create a variable app...that links to the Flask app.  

app = Flask(__name__)  

# Now, set a home page route...  

@app route('/')  

# Create a function that returns a certain value...to be written to the output web page...  

def hw():  
    return 'Hello, world! From Flask app'  

# Finally call the app to run...;  
# and, also, set: debug=True...so, that one can get to read any error output messages...  

if name == __main__:
    app.run(debug=True)
