from flask import Flask  
app = Flask(__name__)  
@app.route('/')  
def hw():  
    return 'Hello, world! From Flask app'  
if __name__ == '__main__':
    app.run(debug=True)
