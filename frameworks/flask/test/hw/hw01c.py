from flask import Flask

app = Flask(__name__)

webPage1='''
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
def hw():
    return webPage1
