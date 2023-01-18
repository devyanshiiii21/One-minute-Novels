
import os
import re

from flask import Flask, render_template, request, url_for, redirect,flash
from flask_mail import Mail, Message
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '4aaba84de24c320143526dd4df3de0dd'
# mail= Mail(app)

# Requires that "Less secure app access" be on
# https://support.google.com/accounts/answer/6010255
# app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_DEFAULT_SENDER')
# app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
# app.config["MAIL_PORT"] = 587
# app.config["MAIL_SERVER"] = "smtp.gmail.com"
# app.config["MAIL_USE_TLS"] = True
# app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
# mail = Mail(app)

posts = [
    {
        'author':'Collen Hoover',
        'title': 'Ugly Love',
        'summary':'lorem ipsum',
        'date_posted': 'January 16th, 2023',
    },
    {
        'author':'Collen Hoover',
        'title': 'Verity',
        'summary':'lorem ipsum',
        'date_posted': 'January 16th, 2023',
    },
    {
        'author':'Collen Hoover',
        'title': 'It Ends With Us',
        'summary':'lorem ipsum',
        'date_posted': 'January 16th, 2023',
    }
]

@app.route("/")
@app.route("/home")
def index():
    return render_template("home.html", posts=posts )

@app.route('/about')
def about():
    return render_template('about.html', title= 'ABOUT')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)