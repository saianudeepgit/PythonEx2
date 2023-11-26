from flask import Flask
app = Flask(__name__)

@app.route('/')
def msg():
    return "Welcome"

@app.route('/vstring/<name>')
def string(name):
    return "My Name is %s" % name
app.run(debug=True)