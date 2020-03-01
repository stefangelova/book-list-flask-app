from application import app, db
from flask import render_template, redirect, url_for
from application.models import Bookss
from application.forms import LoginForm

@app.route('/')
@app.route('/home')
def home():
    postData = Bookss.query.first()
    return render_template('home.html', title='Home', post=postData)
    
@app.route('/about')
def about():
    return render_template('about.html', title='about')
@app.route('/register')
def register():
    return render_template('register.html', title='Register')
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.email.data, form.remember_me.data))
        return redirect('/home')
    return render_template('login.html', title='Login', form=form)
