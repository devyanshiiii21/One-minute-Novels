import os
import re

from cs50 import SQL
from flask_mail import Mail, Message
from flask import Flask, redirect, render_template, request
app = Flask(__name__)

db = SQL("sqlite:///froshims.db")

SPORTS = [
    "Cricket",
    "Football", 
    "Hockey"
]

Registrants = {}

@app.route('/')
def index():
    
    return render_template('index.html', sports=SPORTS)

@app.route('/register', methods=["POST"])
def register():


    #Validate Name
    if not request.form.get("name"):
        return render_template("error.html", message="Missing name")
    
    #Validate Sport
    sport = request.form.get("sport") 
    if not sport:
        return render_template("error.html", message="Missing Sport")
    if sport not in SPORTS:
        return render_template("error.html", message="Invalid Sport")
    
    # #Confirm Registration
    return redirect("/registrants")
    
    #Remenber Registrants 
    Registrants[name] = sport

@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=Registrants)
    