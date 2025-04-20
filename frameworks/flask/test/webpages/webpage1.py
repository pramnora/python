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
  <p>Welcome to my Flask homepage! ;-)</p>
 </body>
</html>
'''

@app.route('/')
def home():
    return homepage

if __name__ == '__main__':
    app.run(debug=True)
