from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class UpdateProfileForm(FlaskForm):
    name = StringField('Real name', validators=[Required()])
    location = StringField('Location', validators=[Required()])
    about_me = TextAreaField('About me')
    submit = SubmitField('Submit')
