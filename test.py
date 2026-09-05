from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/test")
def test():
    word="python"
    return render_template("test.html",word=word)

@app.route("/test1")
def test1():
    return render_template("test1.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    num=44
    return render_template("contact.html",num1=num)
    

if __name__=="__main__":
    app.run(debug=True,port=1234)