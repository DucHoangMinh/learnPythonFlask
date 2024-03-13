from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class RegisterForm(FlaskForm):
    username = StringField(label='Username')
    email_address = StringField(label='Email')
    password1 = PasswordField(label='Password1')
    password2 = PasswordField(label='Password2')
    submit = SubmitField(label='Submit')

