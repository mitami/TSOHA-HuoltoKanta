from flask import render_template, request, url_for, redirect
from application import app, db
from application.models.executor import Executor

@app.route("/executors")
def executors_get_all():
    return render_template(
        "executors/executors.html",
         executors = Executor.query.all()
    )

@app.route("/executors/new")
def executors_new():
    return render_template("executors/new.html")

@app.route("/executor/<id>/edit")
def executors_edit(id):
    item = Executor.query.get(id)
    db.session().commit()

    return render_template("executors/edit.html", executor = item)

@app.route("/executor/<id>")
def executors_get_one(id):
    new = Executor.query.get(id)
    db.session().commit()

    return render_template("executors/executor.html", executor = new)

@app.route("/executor/", methods=["POST"])
def executors_add_one():
    pword = request.form.get("pword")
    name = request.form.get("name")
    title = request.form.get("title")
    if len(pword) < 4 or len(pword) > 20:
        return render_template("executors/new.html", msg = "Password must be 4-20 characters!")
    if len(name) < 2 or len(name) > 20:
        return render_template("executors/new.html", msg = "Username must be 2-20 characters!")
    if len(title) > 30:
        return render_template("executors/new.html", msg = "Title must be under 30 characters!")

    # hash password here
    admin = False
    users = Executor.query.all()
    if not users:
        admin = True
    
    new = Executor(name, title, pword, admin)

    db.session().add(new)
    db.session().commit()

    return render_template("executors/executor.html", executor = new)

@app.route("/executor/<id>/update", methods=["POST"])
def executors_modify_one(id):
    item = Executor.query.get(id)
    #data = request.form
    name = request.form.get("name")
    title = request.form.get("title")

    if len(name) < 2 or len(name) > 20:
        return render_template("executors/edit.html", executor=item, msg = "Username must be 2-20 characters!")
    if len(title) > 30:
        return render_template("executors/edit.html", executor=item, msg = "Title must under 30 characters!")

    item.name = name
    if title:
        item.title = title
    
    db.session().commit()

    return render_template("executors/executor.html", executor = item)

@app.route("/executor/<id>/delete")
def executors_delete_one(id):
    Executor.query.filter_by(id=id).delete()
    db.session().commit()

    return redirect(url_for("executors_get_all"))