from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField, PasswordField, SubmitField
from wtforms.validators import  DataRequired , Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Useraname',validators=[DataRequired(), Length(min=2,max=20)])
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    confirmpassword = PasswordField('Confirm Password',validators=[DataRequired(),EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired()])
    password = PasswordField('Password',validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

