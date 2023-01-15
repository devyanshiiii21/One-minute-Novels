
import os
import re

from flask import Flask, render_template, request
from flask_mail import Mail, Message

app = Flask(__name__)
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
    return render_template("index.html", posts=posts )

@app.route('/about')
def about():
    return render_template('about.html', title= 'ABOUT')

if __name__ == '__main__':
    app.run(debug=True)