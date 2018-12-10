from flask import Flask,request

app = Flask(__name__)

@app.route("/add",methods=["GET","POST"])
def add():
    a = request.values.get("a")
    b = request.values.get("b")
    return str(int(a)+int(b))

app.run()