from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Nume de utilizator', validators=[DataRequired()])
    password = PasswordField('Parolă', validators=[DataRequired()])
    submit = SubmitField('Autentificare')
