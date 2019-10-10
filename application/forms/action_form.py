from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, DateField, validators
from application.utils.constants import msg_action_desc_length, msg_action_name_length

class ActionForm(FlaskForm):
    name = StringField("Nimi", [validators.InputRequired(),
                                validators.length(max=20,
                                                  message=msg_action_name_length)])

    desc = TextAreaField("Kuvaus", [validators.length(max=255,
                                                      message=msg_action_desc_length)])



    class Meta:
        csrf = False