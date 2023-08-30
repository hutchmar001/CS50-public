import os, datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
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


@app.route("/")
@login_required
def index():
    user = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])
    u = user[0]["username"]
    stocks = db.execute("SELECT ALL stock FROM purchases WHERE username = ?;", u)
    print(stocks)
    if stocks:
        for i in stocks:
            st = stocks[i]["stock"]
            print(st)
            shares = db.execute("SELECT SUM(shares) FROM purchases WHERE stock = ? AND username = ?;", st, u)
            sh = shares[i]["SUM(shares)"]
            total = db.execute("SELECT SUM(price) FROM purchases WHERE stock = ? AND username = ?;", st, u)
            sum = total[i]["SUM(price)"]
            a_balance = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])
            ab = a_balance[i]["cash"]
        return render_template("home.html", name=u, stock=st, shares=sh, sum=sum, balance=ab)

    return render_template("home.html")


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        sym = request.form.get("symbol")
        stock = lookup(sym)
        if stock == None:
            return apology("Stock does not exist", 400)

        n = (request.form.get("shares"))
        values = n.split("/")
        if len(values) == 2 and all(i.isdigit() for i in values):
            return apology("Fraction invalid", 400)
        if n.isdigit() == False:
            return apology("Non-numeric invalid", 400)
        if int(n) < 1:
            return apology("Enter a number greater than 0", 400)

        price = stock["price"]
        total_shares = float(request.form.get("shares"))
        total_price = price * total_shares

        a_balance = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])
        a_b = a_balance[0]["cash"]
        if a_b < total_price:
            return apology("You do not have enough money to complete this transaction", 400)

        user = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])
        u = user[0]["username"]
        ct = datetime.datetime.now()
        db.execute("INSERT INTO purchases VALUES (?, ?, ?, ?, ?);", u, sym, total_shares, total_price, ct)
        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        sym = request.form.get("symbol")
        stock = lookup(sym)
        return render_template("quoted.html", name = stock)

    else:
        return render_template("quote.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return apology("must provide username", 400)
        if not request.form.get("password"):
            return apology("must provide password", 400)
        if not request.form.get("confirmation"):
            return apology("must provide password", 400)

        p1 = request.form.get("password")
        p2 = request.form.get("confirmation")
        if p1 != p2:
            return apology("passwords must match", 400)

        u = request.form.get("username")
        repeat = db.execute("SELECT COUNT (*) FROM users WHERE username = ?;", u)
        r = repeat[0]["COUNT (*)"]
        if r > 0:
            return apology("user already exists", 400)

        h = generate_password_hash(password=p1)
        db.execute("INSERT INTO users (username, hash) VALUES (?,?);", u, h)
        session["user_id", 200] = u
        return render_template("login.html")

    else:
        return render_template("register.html")



@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
