from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_required
from application import app, db
from application.models.executor import Executor
from application.models.location import Location

@app.route("/locations")
@login_required
def locations_get_all():
    return render_template("locations/locations.html", locations=Locations.query.all())

@app.route("/location/<id>")
@login_required
def locations_get_one(id):
    location = Location.query.get(id)
    db.session().commit()

    return render_template("locations/location.html", location=location)

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
        return render_template("index.html", msg="Vain Admin voi suorittaa toiminnon!")

    Location.query.filter_by(id=id).delete()
    db.session().commit()

    return redirect(url_for("locations_get_all"))