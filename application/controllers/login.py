from flask import render_template, request, url_for, redirect
from application import app, db
from application.models.executor import Executor

@app.route("/login", methods=["POST"])
def user_login():
    pword = request.form.get("password")
    # hash password here

    user = Executor.query.filter_by(name=request.form.get("name"), password=pword).first()
    if not user:
        return render_template("executors/login.html", msg="No match for credentials entered!")
    
    return redirect(url_for("index"))

@app.route("/login", methods=["GET"])
def render_login():
    return render_template("executors/login.html")