import os
import datetime
import sqlite3

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from operator import itemgetter

# Configure application for each holy book
conn1 = sqlite3.connect('databases/kjv.sqlite', check_same_thread=False)
conn1.row_factory = sqlite3.Row
c1 = conn1.cursor()

conn2 = sqlite3.connect('databases/quran.sqlite3', check_same_thread=False)
conn2.row_factory = sqlite3.Row
c2 = conn2.cursor()

conn3 = sqlite3.connect('databases/bg.sqlite', check_same_thread=False)
conn3.row_factory = sqlite3.Row
c3 = conn3.cursor()

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite databases
db1 = SQL("sqlite:///databases/kjv.sqlite")
db2 = SQL("sqlite:///databases/quran.sqlite3")
db3 = SQL("sqlite:///databases/bg.sqlite")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def index():
    return render_template("home.html", display1="none", display2="none", display3="none", display_select="none", display_img="inline")


@app.route("/search", methods=["GET", "POST"])
def search():

    if request.method == "POST":
        search = request.form.get("search")
        db1.execute("DELETE FROM results;")
        db2.execute("DELETE FROM results;")
        db3.execute("DELETE FROM results;")

        # Bible
        s = db1.execute("SELECT * FROM verses WHERE text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ?", ('% ' + search + ' %'), ('%' + search + ',%'), ('%"' + search + '%'), ('%' + search + '?%'), ('%' + search + '!%'), ('%\'' + search + '%'), ('%' + search + '.%'), ('%.' + search + '%'), ('%' + search + ']%'), ('%' + search + ';%'), ('%,' + search + '%'), ('%' + search + '-%'), ('%-' + search + '%'), ('%(' + search + ')%'))
        # Notice the extra space before/after the %, this ensures that only the complete word is counted as a result
        if s:
            num = 1
            for i in s:
                book = i["book_name"]
                chapter = i["chapter"]
                verse = i["verse"]
                text = i["text"]
                db1.execute("INSERT INTO results VALUES (?, ?, ?, ?, ?);", num, book, chapter, verse, text)
                num += 1

        c1.execute('SELECT * FROM results;')
        lst = []
        for i in c1.fetchall():
            lst.append(dict(i))

        # Quran
        s = db2.execute("SELECT * FROM verses WHERE text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ?", ('% ' + search + ' %'), ('%' + search + ',%'), ('%"' + search + '%'), ('%' + search + '?%'), ('%' + search + '!%'), ('%\'' + search + '%'), ('%' + search + '.%'), ('%.' + search + '%'), ('%' + search + ']%'), ('%' + search + ';%'), ('%,' + search + '%'), ('%' + search + '-%'), ('%-' + search + '%'), ('%(' + search + ')%'))
        # Notice: UPDATE verses SET text = substr(text, instr(text, 'N´')+2); was needed to remove extra text in Quran db
        # Notice: UPDATE results SET text = substr(text, 1, length(text)-2); was needed to remove extra chars at end
        if s:
            num = 1
            for i in s:
                surah = i["sura"]
                verse = i["verse"]
                text = i["text"]
                db2.execute("INSERT INTO results VALUES (?, ?, ?, ?);", num, surah, verse, text)
                num += 1

        c2.execute('SELECT * FROM results;')
        lst2 = []
        for i in c2.fetchall():
            lst2.append(dict(i))

        # Bhagavad Gita
        s = db3.execute("SELECT * FROM verses WHERE text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ?", ('% ' + search + ' %'), ('%' + search + ',%'), ('%"' + search + '%'), ('%' + search + '?%'), ('%' + search + '!%'), ('%\'' + search + '%'), ('%' + search + '.%'), ('%.' + search + '%'), ('%' + search + ']%'), ('%' + search + ';%'), ('%,' + search + '%'), ('%' + search + '-%'), ('%-' + search + '%'), ('%(' + search + ')%'))

        if s:
            num = 1
            for i in s:
                chapter = i["Chapter"]
                verse = i["Verse"]
                text = i["text"]
                db3.execute("INSERT INTO results VALUES (?, ?, ?, ?);", num, chapter, verse, text)
                num += 1

        c3.execute('SELECT * FROM results;')
        lst3 = []
        for i in c3.fetchall():
            lst3.append(dict(i))

        if lst and lst2 and lst3:
            result = ["Bible", "Quran", "Bhagavad Gita"]
            return render_template('home.html', lst=lst, lst2=lst2, lst3=lst3, display1="visible", display2="visible", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result)
        if lst and lst2:
            result = ["Bible", "Quran"]
            return render_template('home.html', lst=lst, lst2=lst2, display1="visible", display2="visible", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result)
        if lst and lst3:
            result = ["Bible", "Bhagavad Gita"]
            return render_template('home.html', lst=lst, lst3=lst3, display1="visible", display2="none", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result)
        if lst2 and lst3:
            result = ["Quran", "Bhagavad Gita"]
            return render_template('home.html', lst2=lst2, lst3=lst3, display1="none", display2="visible", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result)
        if lst:
            result = ["Bible"]
            return render_template('home.html', lst=lst, display1="visible", display2="none", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result)
        if lst2:
            result = ["Quran"]
            return render_template('home.html', lst2=lst2, display1="none", display2="visible", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result)
        if lst3:
            result = ["Bhagavad Gita"]
            return render_template('home.html', lst3=lst3, display1="none", display2="none", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result)

    return render_template("search.html")


@app.route("/All", methods=["GET"])
def All():
    # This route is solely created to deal with the "All" page
    result = ["Bible", "Quran", "Bhagavad Gita"]

    c1.execute('SELECT * FROM results;')
    lst = []
    for i in c1.fetchall():
        lst.append(dict(i))

    result = ["Bible", "Quran", "Bhagavad Gita"]
    c2.execute('SELECT * FROM results;')
    lst2 = []
    for i in c2.fetchall():
        lst2.append(dict(i))

    result = ["Bible", "Quran", "Bhagavad Gita"]
    c3.execute('SELECT * FROM results;')
    lst3 = []
    for i in c3.fetchall():
        lst3.append(dict(i))

    if lst and lst2 and lst3:
        result = ["Bible", "Quran", "Bhagavad Gita"]
        return render_template('home.html', lst=lst, lst2=lst2, lst3=lst3, display1="visible", display2="visible", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result)
    if lst and lst2:
        result = ["Bible", "Quran"]
        return render_template('home.html', lst=lst, lst2=lst2, display1="visible", display2="visible", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result)
    if lst and lst3:
        result = ["Bible", "Bhagavad Gita"]
        return render_template('home.html', lst=lst, lst3=lst3, display1="visible", display2="none", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result)
    if lst2 and lst3:
        result = ["Quran", "Bhagavad Gita"]
        return render_template('home.html', lst2=lst2, lst3=lst3, display1="none", display2="visible", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result)
    if lst:
        result = ["Bible"]
        return render_template('home.html', lst=lst, display1="visible", display2="none", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result)
    if lst2:
        result = ["Quran"]
        return render_template('home.html', lst2=lst2, display1="none", display2="visible", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result)
    if lst3:
        result = ["Bhagavad Gita"]
        return render_template('home.html', lst3=lst3, display1="none", display2="none", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result)


@app.route("/Bible", methods=["GET"])
def Bible():
    result = ["Bible", "Quran", "Bhagavad Gita"]
    c1.execute('SELECT * FROM results;')
    lst = []
    for i in c1.fetchall():
        lst.append(dict(i))
    return render_template('Bible.html', lst=lst, result=result)


@app.route("/Quran", methods=["GET"])
def Quran():
    result = ["Bible", "Quran", "Bhagavad Gita"]
    c2.execute('SELECT * FROM results;')
    lst = []
    for i in c2.fetchall():
        lst.append(dict(i))
    return render_template('Quran.html', lst=lst, result=result)


@app.route("/Bhagavad", methods=["GET"])
def Bhagavad():
    result = ["Bible", "Quran", "Bhagavad Gita"]
    c3.execute('SELECT * FROM results;')
    lst = []
    for i in c3.fetchall():
        lst.append(dict(i))
    return render_template('Bhagavad.html', lst=lst, result=result)


@app.route("/verse", methods=["GET", "POST"])
def verse():

    if request.method == "POST":

        # Bible
        bible_name = request.form.get("bible_name").capitalize()
        bible_chapter = request.form.get("bible_chapter")
        bible_verse = request.form.get("bible_verse")

        if bible_name and bible_chapter and bible_verse:
            lst = db1.execute("SELECT * FROM verses WHERE book_name == ? AND chapter == ? AND verse == ?", bible_name, bible_chapter, bible_verse)
            return render_template('home.html', lst=lst, display1="visible", display2="none", display3="none", display_title="none", display_select="none", display_img="none")

        if bible_name and bible_verse and not bible_chapter:
            return render_template("verse.html")

        if bible_name and bible_chapter:
            lst = db1.execute("SELECT * FROM verses WHERE book_name == ? AND chapter == ?", bible_name, bible_chapter)
            return render_template('home.html', lst=lst, display1="visible", display2="none", display3="none", display_title="none", display_select="none", display_img="none")

        if bible_name:
            lst = db1.execute("SELECT * FROM verses WHERE book_name == ?", bible_name)
            return render_template('home.html', lst=lst, display1="visible", display2="none", display3="none", display_title="none", display_select="none", display_img="none")



        else:
            return render_template("verse.html")

        # Quran
        s = db2.execute("SELECT * FROM verses WHERE text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ?", ('% ' + search + ' %'), ('%' + search + ',%'), ('%"' + search + '%'), ('%' + search + '?%'), ('%' + search + '!%'), ('%\'' + search + '%'), ('%' + search + '.%'), ('%.' + search + '%'), ('%' + search + ']%'), ('%' + search + ';%'), ('%,' + search + '%'), ('%' + search + '-%'), ('%-' + search + '%'), ('%(' + search + ')%'))
        # Notice: UPDATE verses SET text = substr(text, instr(text, 'N´')+2); was needed to remove extra text in Quran db
        # Notice: UPDATE results SET text = substr(text, 1, length(text)-2); was needed to remove extra chars at end
        if s:
            num = 1
            for i in s:
                surah = i["sura"]
                verse = i["verse"]
                text = i["text"]
                db2.execute("INSERT INTO results VALUES (?, ?, ?, ?);", num, surah, verse, text)
                num += 1

        c2.execute('SELECT * FROM results;')
        lst2 = []
        for i in c2.fetchall():
            lst2.append(dict(i))

        # Bhagavad Gita
        s = db3.execute("SELECT * FROM verses WHERE text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ?", ('% ' + search + ' %'), ('%' + search + ',%'), ('%"' + search + '%'), ('%' + search + '?%'), ('%' + search + '!%'), ('%\'' + search + '%'), ('%' + search + '.%'), ('%.' + search + '%'), ('%' + search + ']%'), ('%' + search + ';%'), ('%,' + search + '%'), ('%' + search + '-%'), ('%-' + search + '%'), ('%(' + search + ')%'))

        if s:
            num = 1
            for i in s:
                chapter = i["Chapter"]
                verse = i["Verse"]
                text = i["text"]
                db3.execute("INSERT INTO results VALUES (?, ?, ?, ?);", num, chapter, verse, text)
                num += 1

        c3.execute('SELECT * FROM results;')
        lst3 = []
        for i in c3.fetchall():
            lst3.append(dict(i))

        if lst and lst2 and lst3:
            result = ["Bible", "Quran", "Bhagavad Gita"]
            return render_template('home.html', lst=lst, lst2=lst2, lst3=lst3, display1="visible", display2="visible", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result)
        if lst and lst2:
            result = ["Bible", "Quran"]
            return render_template('home.html', lst=lst, lst2=lst2, display1="visible", display2="visible", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result)
        if lst and lst3:
            result = ["Bible", "Bhagavad Gita"]
            return render_template('home.html', lst=lst, lst3=lst3, display1="visible", display2="none", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result)
        if lst2 and lst3:
            result = ["Quran", "Bhagavad Gita"]
            return render_template('home.html', lst2=lst2, lst3=lst3, display1="none", display2="visible", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result)
        if lst:
            result = ["Bible"]
            return render_template('home.html', lst=lst, display1="visible", display2="none", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result)
        if lst2:
            result = ["Quran"]
            return render_template('home.html', lst2=lst2, display1="none", display2="visible", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result)
        if lst3:
            result = ["Bhagavad Gita"]
            return render_template('home.html', lst3=lst3, display1="none", display2="none", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result)

    return render_template("verse.html")

