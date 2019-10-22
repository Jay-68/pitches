from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError, BooleanField
from wtforms.validators import Required, Email, EqualTo
from ..models import User


class RegistrationForm(FlaskForm):
  '''
  This class passes in the required and email validators
  '''

  email=StringField('Enter Your Email Address',validators=[Required(),Email()])
  username=StringField('Enter Username',validators=[Required()])
  password=PasswordField('Password',validators=[Required(),EqualTo('password',message='password must match')])
  password_confirm=PasswordField('confirm password',validators=[Required()])
  submit=SubmitField('Sign Up')

# custom validators
def validate_email(self,data_field):
  '''
  Function takes in the data field and checks the database to confirm user validation
  '''
  if User.query.filter_by(email=data_field.data).first():
    raise ValidationError('There seems to be an account with that email')

def validate_username(self,data_field):
  '''
  Function checks if the username is unique else it raises a validation error
  '''
  if User.query.filter_by(username=data_field.data).first():
    raise ValidationError('That username is taken')

# log in form with the required fields
class LoginForm(FlaskForm):
  email=StringField('Your Email Address',validators=[Required(),Email()])
  password=PasswordField('password',validators=[Required()])
  remember=BooleanField('Remember me?')
  submit=SubmitField('Sign In')