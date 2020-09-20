from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

csrf = CSRFProtect()


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired('Name cannot be empty')])
    email = StringField('E-mail', validators=[DataRequired('Email cannot be empty'), Email('Enter a valid email')])
    subject = StringField('Subject', validators=[DataRequired('Subject cannot be empty')])
    message = TextAreaField('Message', validators=[DataRequired('Message cannot be empty')])
    submit = SubmitField('SUBMIT')
