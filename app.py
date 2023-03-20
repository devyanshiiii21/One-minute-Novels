
import os
import re

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, url_for, redirect,flash
from flask_mail import Mail, Message
from forms import RegistrationForm, LoginForm
from datetime import datetime

app = Flask(__name__)

app.config['SECRET_KEY'] = '4aaba84de24c320143526dd4df3de0dd'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=True,default='default.jpg')
    password = db.Column(db.String(60),nullable=True)
    posts = db.relationship('Post', backref='author', lazy=True)
    

def __repr(self):
    return f"User('{self.username}','{self.email}','{self.image.jpg}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

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