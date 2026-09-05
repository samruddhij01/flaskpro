from flask import *
import sqlite3 as sq

app = Flask(__name__)
app.secret_key="indiasenkughtgnrktgjnfgiirhrfbnmazigydw23kuhdfibfv "

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    num = 44
    return render_template("contact.html", num1=num)

@app.route("/reg")
def reg():
    return render_template("reg.html")

@app.route("/saveform", methods=["GET", "POST"])
def saveform():
    if request.method == "POST":
        fn = request.form["fullname"]
        em = request.form["email"]
        ps = request.form["password"]
        

        con = sq.connect("login.db")
        cur = con.cursor()
        cur.execute("insert into register(fullname,email,password) values(?,?,?)", (fn, em, ps))
        con.commit()
        con.close()

        return "successfully"
    else:
        return "failed"
    
    
@app.route("/deletestudent/<int:Id>")
def deletestudent(Id):
        con=sq.connect("login.db")
        cur=con.cursor()
        cur.execute("delete from register where Id=?",(Id,))
        con.commit()
        return redirect(url_for("viewdata"))
    
    
    
@app.route("/updatestudent/<int:Id>")
def update(Id):
    con=sq.connect("login.db")
    cur=con.cursor()
    cur.execute("select * from register where Id=?",(Id,))
    data=cur.fetchone()
    return render_template("update.html",data=data)
@app.route("/profileupdate",methods=["GET","POST"])
def profileupdate():
    if request.method=="POST":
        fn=request.form["fullname"]
        em=request.form["email"]
        ps=request.form["password"]
        
        con=sq.connect("login.db")
        cur=con.cursor()
        cur.execute("update register set fullname=?,email=?,password=? where id=?", (fn, em, ps))
        con.commit()
        con.close()
        
        
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="POST":
        em=request.form["email"]
        ps=request.form["password"]
        con=sq.connect("login.db")
        cur=con.cursor()
        data=cur.execute("select * from register where email=? and password=?",(em,ps))
        data=cur.fetchone()
        con.close()
        if data:
            session["username"]=em
            return redirect(url_for("dashboard"))
        else:
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if session.get("username") is not None:
        em=session.get("username")
        con=sq.connect("login.db")
        cur=con.cursor()
        cur.execute("select * from register where email=?",(em,))
        data=cur.fetchone()
        con.close()
        return render_template("dashboard.html",data=data)
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("username",None)
    return redirect(url_for("login"))
    
    
@app.route("/viewdata")
def viewdata():
    con=sq.connect("login.db")
    cur=con.cursor()
    data=cur.execute("select * from register")
    data = cur.fetchall()
    con.close()
    return render_template("viewdata.html",data=data)
if __name__ == "__main__":
    app.run(debug=True, port=1234) 