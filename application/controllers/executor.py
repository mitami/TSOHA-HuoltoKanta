from flask import render_template, request, url_for
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

@app.route("/executors/<id>/edit")
def executors_edit():
    return render_template("executors/edit.html")

@app.route("/executor/<id>")
def executors_get_one():
    return render_template("executors/executor.html")

@app.route("/executor/", methods=["POST"])
def executors_add_one():
    new = Executor(request.form.get("name"), request.form.get("title"))

    db.session().add(new)
    db.session().commit()

    return render_template("executors/executor.html", executor = new)

@app.route("/executor/<id>", methods=["PUT"])
def executors_modify_one():
    return render_template("executors/executor.html")

@app.route("/executor/<id>", methods=["DELETE"])
def executors_delete_one():
    return render_template("executors/executors.html")