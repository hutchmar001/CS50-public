import os
import datetime
import sqlite3

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from operator import itemgetter

# Configure application
conn = sqlite3.connect('kjv.sqlite', check_same_thread=False)
conn.row_factory = sqlite3.Row
c = conn.cursor()
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///kjv.sqlite")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("home.html")


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "POST":
        db.execute("DELETE FROM verses;")
        search = request.form.get("search")
        s = db.execute("SELECT * FROM verses WHERE text LIKE '%" & ? & "%';", search)
        print(s)
        no = s[0]["id"]
        book = s[0]["book"]
        chapter = s[0]["chapter"]
        verse = s[0]["verse"]
        text = s[0]["text"]
        '%" & item & "%' ", con)


        return render_template('home.html', no=no, book=book, chapter=chapter, verse=verse, text=text)

    return render_template("search.html")