from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_required
from application import app, db
from application.models.executor import Executor
from application.models.action import Action
from application.utils.constants import msg_only_admin

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
@login_required
def executors_edit(id):
    if not current_user.get_admin():
        return render_template("index.html", msg=msg_only_admin)
    item = Executor.query.get(id)
    db.session().commit()

    return render_template("executors/edit.html", executor = item)

@app.route("/executor/<id>")
@login_required
def executors_get_one(id):
    user = Executor.query.get(id)
    actions = Executor.get_all_executors_tasks(id)

    db.session().commit()

    return render_template("executors/executor.html", executor = user, actions = actions)

@app.route("/executor/", methods=["POST"])
def executors_add_one():
    #Siivoa tämä?
    if current_user.is_authenticated:
        if not current_user.get_admin():
            return render_template("index.html", msg=msg_only_admin)

    users = db.session.query(Executor).count()
    if users != 0 and not current_user.is_authenticated:
        return render_template("index.html", msg=msg_only_admin)

    print("AMOUNT OF USERS: ")
    print(users)

    pword = request.form.get("pword")
    name = request.form.get("name")
    title = request.form.get("title")
    if len(pword) < 4 or len(pword) > 20:
        return render_template("executors/new.html", msg = "Salasanan pituus oltava 4-20 merkkiä!")
    if len(name) < 2 or len(name) > 20:
        return render_template("executors/new.html", msg = "Käyttäjänimen pituus oltava 2-20 merkkiä!")
    if len(title) > 30:
        return render_template("executors/new.html", msg = "Tittelin maksimipituus on 30 merkkiä!")

    # hash password here
    admin = False
    new = Executor(name, title, pword, admin)
    

    if users == 0:
        admin = True
    
    new.admin = admin

    db.session().add(new)
    db.session().commit()

    return render_template("executors/executor.html", executor = new)

@app.route("/executor/<id>/update", methods=["POST"])
@login_required
def executors_modify_one(id):
    item = Executor.query.get(id)
    name = request.form.get("name")
    title = request.form.get("title")

    if len(name) < 2 or len(name) > 20:
        return render_template("executors/edit.html", executor=item, msg = "Käyttäjänimen pituus oltava 2-20 merkkiä!")
    if len(title) > 30:
        return render_template("executors/edit.html", executor=item, msg = "Tittelin maksimipituus on 30 merkkiä!")

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
    Executor.query.filter_by(id=id).delete()
    db.session().commit()

    return redirect(url_for("executors_get_all"))