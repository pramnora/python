from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
# called using: http://127.0.0.1:5000

@app.route('/page2')
def pageNo2():
    return render_template("page2.html")
# called using: http://127.0.0.1:5000/page2

@app.route('/pages/page3')
def pageNo3():
    return render_template("page3.html")
# called using: http://127.0.0.1:5000/pages/page3

if __name__ == '__main__':
    app.run(debug=True)
