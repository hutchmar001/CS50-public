import os
import datetime
import sqlite3

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from operator import itemgetter

from helpers import apology, login_required, lookup, usd

# Configure application
conn = sqlite3.connect('finance.db', check_same_thread=False)
conn.row_factory = sqlite3.Row
c = conn.cursor()
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    db.execute("DELETE FROM home")
    user = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])
    u = user[0]["username"]

    stocks = db.execute("SELECT DISTINCT stock FROM purchases WHERE username = ?;", u)
    if stocks:
        for i in stocks:
            st = (i.get('stock'))
            stock = lookup(st)

            shares = db.execute("SELECT SUM(shares) FROM purchases WHERE stock = ? AND username = ?;", st, u)
            getter = itemgetter('SUM(shares)')
            gttr = ([getter(item) for item in shares])
            sh = gttr[0]

            shares_sold = db.execute("SELECT SUM(shares) FROM sales WHERE stock = ? AND username = ?;", st, u)
            getter = itemgetter('SUM(shares)')
            gttr = ([getter(item) for item in shares_sold])
            ss = gttr[0]
            if ss != None:
                sh = sh - ss
            if sh == 0:
                continue

            current_price = stock["price"]
            cp = usd(current_price)

            sum = sh * current_price
            sum = usd(sum)

            db.execute("INSERT INTO home VALUES (?, ?, ?, ?, ?);", u, st, sh, cp, sum)

        c.execute('SELECT * FROM home;')
        lst = []
        for i in c.fetchall():
            lst.append(dict(i))

        value_of_shares = db.execute("SELECT SUM(total_price) FROM purchases WHERE username = ?;", u)
        getter = itemgetter('SUM(total_price)')
        gttr = ([getter(item) for item in value_of_shares])
        vs = gttr[0]

        value_sold = db.execute("SELECT SUM(sum) FROM sales WHERE username = ?;", u)
        getter = itemgetter('SUM(sum)')
        gttr = ([getter(item) for item in value_sold])
        vv = gttr[0]
        if vv != None:
            vs = vs - vv
        vs = usd(vs)

        a_balance = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])
        getter = itemgetter('cash')
        gttr = ([getter(item) for item in a_balance])
        ab = gttr[0]
        a = usd(ab)

        return render_template('home.html', u=u, lst=lst, v=vs, a=a)

    return render_template("home.html")
    # Notice that Current Share Price, Value of Shares, and Value of Assets dynamically change over time.
    # Meanwhile Account Balance stays locked to when there was a Buy or Sell.