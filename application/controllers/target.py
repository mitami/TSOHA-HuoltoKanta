from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_required
from application import app, db
from application.models.executor import Executor
from application.models.target import Target


@app.route("/targets")
@login_required
def  targets_get_all():
    return render_template("targets/targets.html", targets = Target.query.all())

@app.route("/targets/<id>")
@login_required
def targets_get_one(id):
    target = Target.query.get(id)
    db.session().commit()

    return render_template("targets/target.html", target = target)

@app.route("/targets/new")
def targets_new():
    return render_template("targets/new.html")

@app.route("/targets/", methods=["POST"])
@login_required
def targets_add_one():
    #Login tagi / annotaatio
    #Tarkista, että käyttäjä on admin?

    #Tässä vaiheessa varmaankin täytyy tehdä linkitys Kohteen ja Sijainnin
    #välille.
    #Älä luo kohdetta, jos tietokannassa ei ole yhtään sijaintia TAI
    #luo kohde ilman sijaintia, ja hoida sijainnittoman kohteen käsittely jotenkin
    name = request.form.get("name")
    new_target = Target(name)
    db.session().add(new_target)
    db.session().commit()

    return render_template("targets/target.html", target = new_target)

@app.route("/targets/<id>/edit")
def targets_edit(id):
    target = Target.query.get(id)
    db.session().commit()

    return render_template("targets/edit.html", target = target)

@app.route("/targets/<id>/update", methods=["POST"])
@login_required
def targets_modify_one(id):
    #Login check
    target = Target.query.get(id)

    #Mahdollisuus 'siirtää' kohde, eli muuttaa sijainti?
    #Nimen validointi
    target.name = request.form.get("name")
    db.session().commit()

    return render_template("targets/target.html", target = target)

@app.route("/targets/<id>/delete")
@login_required
def targets_delete_one(id):
    #Login check
    #Admin check
    target = Target.query.filter_by(id=id).delete()
    db.session().commit()

    return redirect(url_for("targets_get_all"))
