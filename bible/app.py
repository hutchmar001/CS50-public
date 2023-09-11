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
    stocks = db.execute("SELECT * FROM verses WHERE id = 1;")
    print(stocks)
    return render_template("home.html")


@app.route("/choose_verse", methods=["GET", "POST"])
def add_cash():
    if request.method == "POST":

        amount = int(request.form.get("add_cash"))
        cash_balance = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])
        cash_balance = cash_balance[0]["cash"]
        a = cash_balance + amount

        db.execute("UPDATE users SET cash = ? WHERE username = ?;", a, u)
        return redirect("/")

    return render_template("addcash.html")