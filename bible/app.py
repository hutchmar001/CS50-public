import os
import datetime
import sqlite3

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from operator import itemgetter

# Configure application
conn = sqlite3.connect('databases/kjv.sqlite', check_same_thread=False)
conn.row_factory = sqlite3.Row
c = conn.cursor()
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///databases/kjv.sqlite")


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
    db.execute("DELETE FROM results;")
    if request.method == "POST":
        search = request.form.get("search")
        s = db.execute("SELECT * FROM verses WHERE text LIKE ?", ('% ' + search + ' %',))
        # Notice the extra space before/after the %, this ensures that only the complete word is counted as a result

        if s:
            num = 1
            for i in s:
                book = i["book_name"]
                chapter = i["chapter"]
                verse = i["verse"]
                text = i["text"]
                db.execute("INSERT INTO results VALUES (?, ?, ?, ?, ?);", num, book, chapter, verse, text)
                num += 1

        c.execute('SELECT * FROM results;')
        lst = []
        for i in c.fetchall():
            lst.append(dict(i))

        return render_template('home.html', lst=lst)

    return render_template("search.html")