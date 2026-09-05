from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    return"homepage"

@app.route("/name/<str>")
def name(str):
    return "my nane is %s"%str

@app.route("/num/<int:n>")
def num(n):
    return "my number is %d"%n

if __name__=="__main__":
    app.run(debug=True,port=0000)