from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, validators

from application.utils.constants import msg_target_name_length, msg_target_no_loc, msg_target_no_name

class TargetForm(FlaskForm):
    name = StringField("Nimi", [validators.InputRequired(message=msg_target_no_name),
                                validators.Length(min=2,
                                                  max=20,
                                                  message=msg_target_name_length)])

    class Meta:
        csrf = False