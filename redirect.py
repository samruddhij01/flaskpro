from flask import *
app=Flask(__name__)

@app.route("/")
def home():
    return "homepage"
@app.route("/about")
def about():
    return redirect(url_for("contact"))

@app.route("/contact")
def contact():
    return "contant us"
if __name__=="__main__":
    app.run(debug=True,port=1000)
    

