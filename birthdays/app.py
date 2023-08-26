import os, sys, time

from cs50 import SQL
from flask import *

# Configure application
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        # TODO: Add the user's entry into the database
        n = request.form.get("name")
        m = request.form.get("month")
        d = request.form.get("day")
        if int(m) < 0 or int(d) < 0:
            session.pop('_flashes', None)
            flash('Please enter a value greater than 0.')
            return redirect("/")
        sys.stdout.write(__name__) # Prints name of value into terminal
        db.execute("INSERT INTO birthdays (name, month, day) VALUES (?, ?, ?)", n, m, d)
        return redirect("/")

    else:
        # TODO: Display the entries in the database on index.html
        result = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", result=result)

@app.route('/delete/')
def delete():
  db.execute("DELETE FROM birthdays")
  result = db.execute("SELECT * FROM birthdays")
  return render_template("index.html", result=result)

