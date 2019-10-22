from flask import render_template, redirect, url_for, request, flash
from . import auth
from flask_login import login_user, logout_user, login_required
from .views import RegistrationForm,loginForm
# from ..models import RegistrationForm, loginForm
from .. import db

# registration route
@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))
        title = 'New Account'
    return render_template('auth/register.html', registration_form=form)


# login form
@auth.route('/login',methods=['GET','POST'])
def login():
  '''
  Function that checks if the form is validated
  '''
  login_form=loginForm()
  if login_form.validate_on_submit():
    user=User.query.filter_by(email=login_form.email.data).first()
    if user is not None and user.verify_password(login_form.password.data):
      login_user(user,login_form.remember.data)
      return redirect(request.args.get('Next') or url_for('main.index'))

    flash('Invalid username or password')

  title='Pitches Log In'
  return render_template('auth/login.html',login_form=login_form,title=title)

  