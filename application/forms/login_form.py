from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class TaskForm(FlaskForm):
    name = StringField("Nimi")
    pword = PasswordField("Salasana")

    class Meta:
        csrf = False