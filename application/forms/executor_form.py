from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

from application.utils.constants import msg_executor_title_length, msg_executor_name_length, msg_password_match, msg_password_length

class ExecutorForm(FlaskForm):
    name = StringField("Nimi", [validators.InputRequired(),
                                validators.length(min=2, max=20, message=msg_executor_name_length)])
    title = StringField("Titteli", [validators.length(max=30, message=msg_executor_title_length)])
    pword = PasswordField("Salasana", [validators.InputRequired(),
                                       validators.EqualTo('pwordagain',
                                                          message=msg_password_match),
                                       validators.length(min=4, max=20, message=msg_password_length)])
    pwordagain = PasswordField("Salasana uudelleen", [validators.InputRequired(),
                                                      validators.length(min=4, max=20, message=msg_password_length)])


    class Meta:
        csrf = False