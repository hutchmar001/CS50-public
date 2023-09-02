import os, datetime, sqlite3

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

            shares = db.execute("SELECT SUM(shares) FROM purchases WHERE stock = ? AND username = ?;", st, u)
            getter = itemgetter('SUM(shares)')
            gttr = ([getter(item) for item in shares])
            sh = gttr[0]

            stock = lookup(st)
            current_price = stock["price"]
            cp = usd(current_price)

            sum = sh * current_price
            s = usd(sum)

            db.execute("INSERT INTO home VALUES (?, ?, ?, ?, ?);", u, st, sh, cp, s)

        c.execute('SELECT * FROM home;')
        lst = []
        for i in c.fetchall():
            lst.append(dict(i))

        value_of_shares = db.execute("SELECT SUM(total_price) FROM purchases WHERE username = ?;", u)
        getter = itemgetter('SUM(total_price)')
        gttr = ([getter(item) for item in value_of_shares])
        vs = gttr[0]
        v = usd(vs)

        a_balance = db.execute("SELECT cash FROM users WHERE id = ?;", session["user_id"])
        getter = itemgetter('cash')
        gttr = ([getter(item) for item in a_balance])
        ab = gttr[0]
        a = usd(ab)

        return render_template('home.html', u=u, lst=lst, v=v, a=a)

    return render_template("home.html")
    # Notice that Current Share Price, Value of Shares, and Value of Assets dynamically change over time.
    # Meanwhile Account Balance stays locked to when there was a Buy or Sell.

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    user = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])
    u = user[0]["username"]

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

        a_b = a_b - total_price
        db.execute("UPDATE users SET cash = ? WHERE username = ?;", a_b, u)
        ct = datetime.datetime.now()
        db.execute("INSERT INTO purchases VALUES (?, ?, ?, ?, ?, ?);", u, sym, total_shares, price, total_price, ct)
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
        if len(sym) == 0:
            return apology("Blank ticker", 400)
        stock = lookup(sym)
        if stock == None:
            return apology("Invalid ticker", 400)
        s = stock["price"]
        price = usd(s)

        return render_template("quoted.html", name = price)

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
    user = db.execute("SELECT username FROM users WHERE id = ?;", session["user_id"])
    u = user[0]["username"]

    if request.method == "POST":
        sym = request.form.get("symbol")
        stock = lookup(sym)

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

        stock = stock["name"].lower()
        st = db.execute("SELECT shares FROM home WHERE stock = ?;", stock)
        if not st:
            return apology("You do not have any shares of this stock", 400)
        shares = st[0]["shares"]
        if shares < total_shares:
            return apology("You do not have enough shares to sell", 400)
        shares_update = int(shares - total_shares)
        db.execute("UPDATE home SET 'shares' = ? WHERE stock = ?;", shares_update, stock)

        a_b = a_b + total_price
        print(stock)
        print(shares_update)
        db.execute("UPDATE users SET cash = ? WHERE username = ?;", a_b, u)
        ct = datetime.datetime.now()
        db.execute("INSERT INTO sales VALUES (?, ?, ?, ?, ?, ?);", u, stock, total_shares, price, total_price, ct)
        return redirect("/")

    else:
        stock_select = db.execute("SELECT stock FROM home;")
        result = [ i['stock'] for i in stock_select ]

        return render_template("sell.html", result=result)
