from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_required
from application import app, db
from application.models.executor import Executor
from application.models.location import Location
from application.models.target import Target
from application.utils.constants import msg_only_admin
from application.forms.location_form import LocationForm

@app.route("/locations")
@login_required
def locations_get_all():
    return render_template("locations/locations.html", locations=Location.query.all())

@app.route("/location/<id>")
@login_required
def locations_get_one(id):
    location = Location.query.get(id)
    targets = Target.query.filter_by(location_id = id)
    db.session().commit()

    return render_template("locations/location.html", location=location, targets=targets)

@app.route("/locations/new")
@login_required
def locations_new():
    return render_template("locations/new.html", form=LocationForm())

@app.route("/location/<id>/edit")
@login_required
def locations_edit(id, messages=[]):
    location = Location.query.get(id)
    db.session().commit()
    return render_template("locations/edit.html",
                            location=location,
                            form=LocationForm(obj=location),
                            messages=messages)

@app.route("/location/<id>/delete")
@login_required
def locations_delete_one(id):
    if not current_user.get_admin():
        return render_template("index.html", msg=msg_only_admin)

    Location.query.filter_by(id=id).delete()
    db.session().commit()

    return redirect(url_for("locations_get_all"))

@app.route("/location/", methods=["POST"])
@login_required
def locations_add_one():
    if not current_user.get_admin():
        return render_template("index.html", msg=msg_only_admin)

    form = LocationForm(request.form)
    
    messages = []
    if not form.validate():
        return render_template("locations/new.html",  form=form)

    name = request.form.get("name")

    
    location = Location(name)
    db.session().add(location)
    db.session().commit()
    return render_template("locations/location.html",
                            location=location)

@app.route("/location/<id>/update", methods=["POST"])
@login_required
def locations_modify_one(id):
    if not current_user.get_admin():
        return render_template("index.html", msg=msg_only_admin)

    form = LocationForm(request.form)
    messages = []
    
    if not form.validate():
        return render_template("locations/edit.html",
                                form=form,
                                location=Location.query.get(id))


    name = request.form.get("name")
    loc = Location.query.get(id)
    loc.name = name
    db.session().commit()
    
    return redirect(url_for('locations_get_one', id=id))
    
