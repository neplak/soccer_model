from flask_wtf import FlaskForm
from wtforms import Form, SubmitField,StringField, TextAreaField, SelectField, validators
from wtforms.fields.core import IntegerField,StringField


class TeamForm(FlaskForm):
    name = StringField('Name', [validators.Length(min=2,max=50),
                                validators.DataRequired(message='Force is required')])
    location = StringField('Location', [validators.Length(min=2,max=50),
                                        validators.DataRequired(message='Force is required')])
    force=IntegerField('Force',[validators.NumberRange(min=50,max=100,message='Required value between 50 and 100'),
                                validators.DataRequired(message='Force field is required')])
    submit = SubmitField('Submit')
    
class ScheduleForm(FlaskForm):
    submit = SubmitField('Play')

