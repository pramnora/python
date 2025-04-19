from flask import Flask

app = Flask(__name__)

outputString='Hello, world! From Flask app'

@app.route('/')
def hw():
    return outputString

if __name__ == '__main__':
    app.run(debug=True)
