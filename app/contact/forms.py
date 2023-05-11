from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Length, Email

class ContactMe(FlaskForm):
    name = StringField('Your Name', validators=[InputRequired(),
                                                Length(min=3, max=100)])
    email = StringField('Your Email', validators=[Email(), InputRequired()])
    message = TextAreaField('Message',
                            validators=[InputRequired(),
                                        Length(max=200)])
    recaptcha = RecaptchaField()
    submit = SubmitField('Send')