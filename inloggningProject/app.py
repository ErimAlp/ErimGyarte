from flask import Flask, render_template, request, redirect, url_for
import bcrypt
from db.index import db

#from markupsafe import escape

app = Flask(__name__, static_folder="web/static", template_folder="web/templates")

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/style.css")
def style():
    return app.send_static_file("style.css")
    
@app.route("/user/<username>")
def display_user(username=None):
    return render_template("user.html", name=username)

@app.route("/login", methods=["POST", "GET"])
def login():
    if  request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        login_database(username, password)
    elif request.method == "GET":
        pass
    
    return render_template("user.html", name=username)

@app.route("/register", methods=["POST"])
def register():
    username = request.form["username"]
    password = request.form["password"]
    create_account(username, password)

    return redirect(url_for("index"))
    
def create_account(username, password):
    password = password.encode()
    hash_password = bcrypt.hashpw(password, bcrypt.gensalt())
    # print(username, password,)
    user = {"name": username, 
    "password": hash_password.decode() }
    db.child("users").push(user)
    print(user)

def login_database(username, password):
    db_user = db.child("users").order_by_child("name").equal_to(username).get().val().values()
    db_user = list(db_user)[0]
    print(db_user)
    password = password.encode()
    hash_pw = db_user["password"].encode()

    if bcrypt.checkpw(password, hash_pw):
        print("logged in")

    else:
        print("wrong password")
