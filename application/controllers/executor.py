from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_required
from application import app, db
from application.models.executor import Executor
from application.models.action import Action
from application.utils.constants import msg_only_admin

from application.forms.executor_form import ExecutorForm
import datetime

@app.route("/executors")
def executors_get_all():
    return render_template(
        "executors/executors.html",
         executors = Executor.query.all()
    )

@app.route("/executors/new")
def executors_new():
    return render_template("executors/new.html", form=ExecutorForm())

@app.route("/executor/<id>/edit")
@login_required
def executors_edit(id):
    if not current_user.get_admin():
        return render_template("index.html", msg=msg_only_admin)
    executor = Executor.query.get(id)
    db.session().commit()

    return render_template("executors/edit.html",
                            executor = executor,
                            form=ExecutorForm(obj=executor))

@app.route("/executor/<id>")
@login_required
def executors_get_one(id):
    user = Executor.query.get(id)
    actions = Executor.get_all_executors_tasks(id)

    amounts = {}
    undone = Executor.get_amount_of_executors_undone_tasks(id)
    done = Executor.get_amount_of_executors_done_tasks(id)
    db.session().commit()
    amounts['undone'] = undone[0]
    amounts['done'] = done[0]

    return render_template("executors/executor.html", executor = user, actions = actions, amounts = amounts)

@app.route("/executor/", methods=["POST"])
def executors_add_one():
    #Siivoa tämä?
    if current_user.is_authenticated:
        if not current_user.get_admin():
            return render_template("index.html", msg=msg_only_admin)

    users = db.session.query(Executor).count()
    if users != 0 and not current_user.is_authenticated:
        return render_template("index.html", msg=msg_only_admin)

    pword = request.form.get("pword")
    name = request.form.get("name")
    existing = Executor.query.filter_by(name = name).first()
    if existing:
        return render_template("executors/new.html", msg = "Käyttäjänimi on jo käytössä")


    form = ExecutorForm(request.form)
    if not form.validate():
        return render_template("executors/new.html", form=form)

    title = request.form.get("title")
    
    # hash password here
    admin = False
    new = Executor(name, title, pword, admin)
    

    if users == 0:
        admin = True
    
    new.admin = admin

    db.session().add(new)
    db.session().commit()

    return redirect(url_for('executors_get_one', id = new.id))

@app.route("/executor/<id>/update", methods=["POST"])
@login_required
def executors_modify_one(id):
    item = Executor.query.get(id)
    name = request.form.get("name")
    title = request.form.get("title")

    form = ExecutorForm(request.form)
    if not form.validate():
        return render_template("executors/edit.html", form=form)

    item.name = name
    if title:
        item.title = title
    
    db.session().commit()

    return render_template("executors/executor.html", executor = item)

@app.route("/executor/<id>/delete")
@login_required
def executors_delete_one(id):
    if not current_user.get_admin():
        return render_template("index.html", msg=msg_only_admin)
    #ADMIN-käyttäjän poistaminen on estetty toistaiseksi kokonaan
    user = Executor.query.get(id)
    if user.admin:
        db.session().commit()
        return render_template("index.html", msg="Admin käyttäjien poistaminen ei ole mahdollista!")
    to_be_deleted = Executor.query.filter_by(id=id).first()
    db.session().delete(to_be_deleted)
    db.session().commit()

    return redirect(url_for("executors_get_all"))

@app.route("/executor/<e_id>/action/<a_id>/toggle")
@login_required
def executors_toggle_done_from_own_list(e_id, a_id):
    action = Action.query.get(a_id)
    # Tarkistetaanko onko tehtävä käyttäjän oma?
    if not action.done:
        action.done = True
    else:
        action.done = False

    db.session().commit()

    return redirect(url_for('executors_get_one', id = e_id))
