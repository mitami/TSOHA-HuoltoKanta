from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_required
from application import app, db
from application.models.executor import Executor
from application.models.action import Action
from application.models.target import Target
from application.utils.constants import msg_only_admin

from application.forms.action_form import ActionForm
import datetime

@app.route("/actions/")
@login_required
def actions_get_all():
    actions = Action.query.order_by(Action.due).all()

    return render_template("actions/actions.html", actions = actions)

@app.route("/action/<id>")
@login_required
def actions_get_one(id):
    #Näytetään Tehtävän näkymässä Tehtävän Kohde, sekä Käyttäjä, jolle Tehtävä on
    #merkitty/kuka tehtävän on luonut.
    data = Action.find_one_with_target_and_user(id)
    #action = Action.query.get(id)
    print("<<<<<---------------Käyttäjä(t)--------->>>>>>>>>>>>>>>")
    print(data[0])
    for item in data:
        print(item)
        print("-------------")

    return render_template("actions/action.html", data = data[0])

@app.route("/actions/new")
@login_required
def actions_new():
    targets = Target.query.all()
    executors = Executor.query.all()

    form = ActionForm()
    return render_template("actions/new.html",
                           targets=targets,
                           form=form,
                           executors=executors)

@app.route("/actions/<id>/done")
@login_required
def actions_toggle_done(id):
    action = Action.query.get(id)
    if not action.done:
        action.done = True
    else:
        action.done = False

    db.session().commit()

    return redirect(url_for("actions_get_one", id=action.id))

@app.route("/actions/<id>/toggle")
@login_required
def actions_toggle_from_list(id):
    action = Action.query.get(id)
    if not action.done:
        action.done = True
    else:
        action.done = False

    db.session().commit()

    return redirect(url_for("actions_get_all"))

@app.route("/actions/<id>/edit")
@login_required
def actions_edit(id):
    action = Action.query.get(id)
    db.session().commit()
    targets = Target.query.all()
    executors = Executor.query.all()

    form = ActionForm(obj=action)

    return render_template("actions/edit.html",
                            action=action,
                            targets=targets,
                            executors=executors,
                            form=form)

@app.route("/actions/<id>/delete")
@login_required
def actions_delete_one(id):
    if not current_user.get_admin():
        return render_template("index.html", msg=msg_only_admin)

    to_be_deleted = Action.query.filter_by(id=id).first()
    db.session().delete(to_be_deleted)
    db.session().commit()

    return redirect(url_for('actions_get_all'))

@app.route("/actions/<id>/update", methods=["POST"])
@login_required
def actions_modify_one(id):
    name = request.form.get("name")
    desc = request.form.get("desc")
    due = request.form.get("due")
    target_id = request.form.get("target")
    executors = request.form.getlist("executors")

    action = Action.query.get(id)

    form = ActionForm(request.form)

    if not form.validate():
        return render_template("actions/edit.html",
                                action=action,
                                targets=Target.query.all(),
                                form=form)
    
    action.name = name
    action.desc = desc
    action.target_id = target_id
    if due:
        due = datetime.datetime.strptime(due, '%Y-%m-%d')
        due = due.date()
        action.due = due

    if executors:
        executors = [Executor.query.get(e) for e in executors]
        action.executors = executors

    db.session().commit()

    return redirect(url_for('actions_get_one', id = id))

@app.route("/actions/", methods=["POST"])
@login_required
def actions_add_one():
    executor = Executor.query.get(current_user.id)
    executors = request.form.getlist("executors")
    name = request.form.get("name")
    desc = request.form.get("desc")
    due = request.form.get("due")
    done = False

    form = ActionForm(request.form)
    if not form.validate():
        render_template("actions/new.html",
                        form=form,
                        targets=Target.query.all())

    if due:
        due = datetime.datetime.strptime(due, '%Y-%m-%d')
        due = due.date()

    target_id = request.form.get("target")
    new = Action(name, desc, due, done, target_id)

    #Lisätään Toimenpide Käyttäjän toimenpiteet -listaan
    #executor.actions.append(new)
    db.session.add(new)
    db.session().flush()

    action = Action.query.get(new.id)
    executors = [Executor.query.get(e) for e in executors]

    action.executors = executors
    db.session().commit()

    return redirect(url_for("actions_get_one", id = new.id))