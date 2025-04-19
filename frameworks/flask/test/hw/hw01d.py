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
  <title>Page 2</title>
 </head>
 <body>
  <p>Welcome to Page 2!</p>
 </body>
</html>
'''

page3='''
<!DOCTYPE html>
<html lang="en">
 <head>
  <meta charset="UTF-8">
  <title>Page 3</title>
 </head>
 <body>
  <p>Welcome to Page 3!</p>
 </body>
</html>
'''

@app.route('/')
def home():
    return homepage
# called using: http://127.0.0.1:5000

@app.route('/page2')
def pageNo2():
    return page2
# called using: http://127.0.0.1:5000/page2

@app.route('/pages/page3')
def pageNo3():
    return page3
# called using: http://127.0.0.1:5000/pages/page3

if __name__ == '__main__':
    app.run(debug=True)  
