from flask_wtf import FlaskForm
from wtforms import StringField, validators
from application.utils.constants import msg_loc_name_legth, msg_loc_no_name

class LocationForm(FlaskForm):
    name = StringField("Nimi", [validators.InputRequired(message=msg_loc_no_name),
                                validators.Length(min=2,
                                                  max=30,
                                                  message=msg_loc_name_legth)])

    class Meta:
        csrf = False