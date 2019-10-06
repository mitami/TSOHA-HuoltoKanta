from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_required
from application import app, db
from application.models.executor import Executor
from application.models.location import Location
from application.models.target import Target
from application.utils.constants import msg_only_admin, msg_loc_name_legth, msg_loc_no_name

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
    return render_template("locations/new.html")

@app.route("/location/<id>/edit")
@login_required
def locations_edit(id):
    location = Location.query.get(id)
    db.session().commit()
    return render_template("locations/edit.html", location=location)

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

    name = request.form.get("name")
    messages = []
    if not name:
        messages.append(msg_loc_no_name)
        return render_template("locations/new.html",  messages=messages)
    
    if len(name) <= 30 and len(name) > 1:
        location = Location(name)
        db.session().add(location)
        db.session().commit()
        return render_template("locations/location.html",
                                location=location)

    messages.append(msg_loc_name_legth)
    return render_template("locations/new.html",  messages=messages)

@app.route("/location/<id>/update", methods=["POST"])
@login_required
def locations_modify_one(id):
    if not current_user.get_admin():
        return render_template("index.html", msg=msg_only_admin)

    name = request.form.get("name")
    loc = Location.query.get(id)

    messages = []
    if not name:
        messages.append(msg_loc_no_name)
        return render_template("locations/edit.html",
                                location=loc,
                                messages=messages)
    
    if len(name) <= 30 and len(name) > 1:
        loc.name = name
        db.session().commit()
        return render_template("locations/location.html", location=loc)
    else:
        targets = Target.query.filter_by(location_id = id)
        messages.append(msg_loc_name_legth)
        return render_template("locations/location.html",
                                location=loc,
                                targets=targets,
                                messages=messages)
    
