from flask import Flask

app = Flask(__name__)

homepage='''
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="UTF-8">
  <title>Homepage</title>
 </head>
 <body>
  <p>Welcome to my Flask homepage!</p>
 </body>
</html>
'''

page2='''
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="UTF-8">
  <title>page2</title>
 </head>
 <body>
  <p>Welcome to page2...! ;-)</p>
 </body>
</html>
'''

@app.route('/')
def home():
    return homepage

@app.route('/page2')
def home():
    return page2

if __name__ == '__main__':
    app.run(debug=True)
