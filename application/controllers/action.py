from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_required
from application import app, db
from application.models.executor import Executor
from application.models.action import Action
from application.models.target import Target

from datetime import datetime

@app.route("/actions/")
@login_required
def actions_get_all():
    actions = Action.query.all()

    return render_template("actions/actions.html", actions = actions)

@app.route("/actions/<id>")
@login_required
def actions_get_one(id):
    action = Action.query.get(id)

    return render_template("actions/action.html", action = action)

@app.route("/actions/new")
@login_required
def actions_new():
    targets = Target.query.all()
    return render_template("actions/new.html", targets=targets)

@app.route("/actions/", methods=["POST"])
@login_required
def actions_add_one():
    executor = Executor.query.get(current_user.id)
    name = request.form.get("name")
    desc = request.form.get("desc")
    due = request.form.get("due")
    done = False
    if due:
        due = datetime.strptime(due, '%Y-%m-%d')
        due = due.date()
    #todo liitostaulun teko oikein, ja uuden actionin luominen sen mukaan


    target_id = request.form.get("target_id")
    new = Action(name, desc, due, done)

    #db.session().add(new)
    executor.actions.append(new)
    db.session().commit()

    return render_template("actions/action.html", action = new)

@app.route("/actions/<id>/edit")
@login_required
def actions_edit(id):
    action = Actions.query.get(id)
    db.session().commit()

    return render_template("actions/edit.html", action = action)

@app.route("/actions/<id>/update", methods=["POST"])
@login_required
def actions_modify_one(id):
    name = request.form.get("name")
    desc = request.form.get("desc")
    due = request.form.get("due")

    action = Action.query.get(id)

    if name:
        action.name = name
    if desc:
        action.desc = desc
    if due:
        action.due = due

    db.session().commit()

    return redirect(url_for('actions_get_one', id = id))

@app.route("/actions/<id>/delete")
@login_required
def actions_delete_one(id):
    Action.query.filter_by(id=id).delete()
    db.session().commit()

    return redirect(url_for('actions_get_all'))