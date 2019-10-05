from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_required
from application import app, db
from application.models.executor import Executor
from application.models.target import Target
from application.models.action import Action
from application.models.location import Location
from application.utils.constants import msg_only_admin


@app.route("/targets")
@login_required
def  targets_get_all():
    return render_template("targets/targets.html", targets = Target.query.all())

@app.route("/targets/<id>")
@login_required
def targets_get_one(id):
    #target = Target.find_target_and_its_location(id)
    target = Target.find_target_and_its_location(id)
    actions = Target.find_related_actions(id)
    #Tarkista vastaus, jos tyhjä, palauta viesti.
    db.session().commit()

    return render_template("targets/target.html", target=target[0], actions=actions)

@app.route("/targets/new")
@login_required
def targets_new():
    locations = Location.query.all()
    db.session().commit()
    return render_template("targets/new.html", locations=locations)

@app.route("/targets/", methods=["POST"])
@login_required
def targets_add_one():
    #Tarkista, että käyttäjä on admin?
    if not current_user.get_admin():
        return render_template("index.html", msg=msg_only_admin)

    #Tässä vaiheessa varmaankin täytyy tehdä linkitys Kohteen ja Sijainnin
    #välille.
    #Älä luo kohdetta, jos tietokannassa ei ole yhtään sijaintia TAI
    #luo kohde ilman sijaintia, ja hoida sijainnittoman kohteen käsittely jotenkin
    name = request.form.get("name")
    location = request.form.get("location")
    new_target = Target(name, location)
    #new_target.location_id = location
    db.session().add(new_target)
    db.session().commit()

    return redirect(url_for("targets_get_one", id=new_target.id))

@app.route("/targets/<id>/edit")
@login_required
def targets_edit(id):
    locations = Location.query.all()
    
    target = Target.query.get(id)
    db.session().commit()

    return render_template("targets/edit.html", target = target, locations=locations)

@app.route("/targets/<id>/update", methods=["POST"])
@login_required
def targets_modify_one(id):
    if not current_user.get_admin():
        return render_template("index.html", msg=msg_only_admin)

    target = Target.query.get(id)

    #Nimen validointi
    name = request.form.get("name")
    location = request.form.get("location")
    if name:
        target.name = name
    if location:
        target.location_id = location
    db.session().commit()

    return redirect(url_for("targets_get_one", id = target.id))

@app.route("/targets/<id>/delete")
@login_required
def targets_delete_one(id):
    if not current_user.get_admin():
        return render_template("index.html", msg=msg_only_admin)

    target = Target.query.filter_by(id=id).delete()
    db.session().commit()

    return redirect(url_for("targets_get_all"))

@app.route("/target/<t_id>/action/<a_id>/toggle")
@login_required
def targets_toggle_done_from_own_list(t_id, a_id):
    action = Action.query.get(a_id)
    # Tarkistetaanko onko tehtävä käyttäjän oma?
    if not action.done:
        action.done = True
    else:
        action.done = False

    db.session().commit()

    return redirect(url_for('targets_get_one', id = t_id))
