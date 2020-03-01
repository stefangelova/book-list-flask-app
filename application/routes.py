from application import app, db, bcrypt
from application.models import Bookss, User
from flask_login import login_user, current_user, logout_user, login_required
from application.forms import RegistrationForm, LoginForm
from flask import render_template, redirect, url_for, request

@app.route('/')
@app.route('/home')
def home():
    postData = Bookss.query.first()
    return render_template('home.html', title='Home', post=postData)

@app.route('/about')
def about():
    return render_template('about.html', title='about')
@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_pw = bcrypt.generate_password_hash(form.password.data.decode('utf-8'))

        user = User(email=form.email.data, password=hash_pw)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('post'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
