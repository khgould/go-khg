from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (StringField, SubmitField)
from wtforms.validators import InputRequired, Email


class ResumeForm(FlaskForm):
    email_address = StringField('Your Email', validators=[Email(), InputRequired()])
    recaptcha = RecaptchaField()
    submit = SubmitField('Submit')