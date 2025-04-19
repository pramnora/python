from flask import Flask

app = Flask(__name__)

homepage='''
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="UTF-8">
  <title>Web page testing...</title>
 </head>
 <body>
  <p>This is my 1st Flask web page...! ;-)</p>
 </body>
</html>
'''

@app.route('/')
def home():
    return webPage1

if __name__ == '__main__':
    app.run(debug=True)
