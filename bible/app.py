import sqlite3

from cs50 import SQL
from flask import Flask, render_template, request, flash, redirect
from flask_session import Session
from common import cache

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
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
cache.init_app(app=app, config={"CACHE_TYPE": "filesystem",'CACHE_DIR': 'cache-dir'})

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
    return render_template("home.html", display1="none", display2="none", display3="none", display_select="none", display_img="inline", search_upper="", search_lower="", rpp_search="none")
    # set searches to "" to avoid JSON error

@app.route("/search", methods=["GET", "POST"])
def search():

    if request.method == "POST":
        search = request.form.get("search")
        if not search or search == " ":
            flash('Please enter a valid query.')
            return redirect("/search")
        search_lower = search.lower()
        search_upper = search.title()
        rpp = request.form.get("rpp")
        if not rpp:
            rpp = 20

        # Bible
        lst = db1.execute("SELECT * FROM verses WHERE text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ?;", ('% ' + search + ' %'), ('%' + search + ',%'), ('%"' + search + '%'), ('%' + search + '?%'), ('%' + search + '!%'), ('%\'' + search + '%'), ('%' + search + '.%'), ('%.' + search + '%'), ('%' + search + ']%'), ('%' + search + ';%'), ('%,' + search + '%'), ('%' + search + '-%'), ('%-' + search + '%'), ('%(' + search + ')%'))
        # Notice the extra space before/after the %, this ensures that only the complete word is counted as a result

        # Quran
        lst2 = db2.execute("SELECT * FROM verses WHERE text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ?;", ('% ' + search + ' %'), ('%' + search + ',%'), ('%"' + search + '%'), ('%' + search + '?%'), ('%' + search + '!%'), ('%\'' + search + '%'), ('%' + search + '.%'), ('%.' + search + '%'), ('%' + search + ']%'), ('%' + search + ';%'), ('%,' + search + '%'), ('%' + search + '-%'), ('%-' + search + '%'), ('%(' + search + ')%'))
        # Notice: UPDATE verses SET text = substr(text, instr(text, 'N´')+2); was needed to remove extra text in Quran db
        # Notice: UPDATE results SET text = substr(text, 1, length(text)-2); was needed to remove extra chars at end

        # Bhagavad Gita
        lst3 = db3.execute("SELECT * FROM verses WHERE text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? OR text LIKE ? \
            OR text LIKE ?;", ('% ' + search + ' %'), ('%' + search + ',%'), ('%"' + search + '%'), ('%' + search + '?%'), ('%' + search + '!%'), ('%\'' + search + '%'), ('%' + search + '.%'), ('%.' + search + '%'), ('%' + search + ']%'), ('%' + search + ';%'), ('%,' + search + '%'), ('%' + search + '-%'), ('%-' + search + '%'), ('%(' + search + ')%'))

        cache.set("lst", lst)
        cache.set("lst2", lst2)
        cache.set("lst3", lst3)
        cache.set("search_lower", search_lower)
        cache.set("search_upper", search_upper)

        if lst and lst2 and lst3:
            result = ["Bible", "Quran", "Bhagavad Gita"]
            return render_template('home.html', lst=lst, lst2=lst2, lst3=lst3, display1="visible", display2="visible", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_lower = search_lower, search_upper = search_upper, rpp=rpp)
        if lst and lst2:
            result = ["Bible", "Quran"]
            return render_template('home.html', lst=lst, lst2=lst2, display1="visible", display2="visible", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result, search_lower = search_lower, search_upper = search_upper, rpp=rpp)
        if lst and lst3:
            result = ["Bible", "Bhagavad Gita"]
            return render_template('home.html', lst=lst, lst3=lst3, display1="visible", display2="none", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_lower = search_lower, search_upper = search_upper, rpp=rpp)
        if lst2 and lst3:
            result = ["Quran", "Bhagavad Gita"]
            return render_template('home.html', lst2=lst2, lst3=lst3, display1="none", display2="visible", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_lower = search_lower, search_upper = search_upper, rpp=rpp)
        if lst:
            result = ["Bible"]
            return render_template('home.html', lst=lst, display1="visible", display2="none", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result, search_lower = search_lower, search_upper = search_upper, rpp=rpp)
        if lst2:
            result = ["Quran"]
            return render_template('home.html', lst2=lst2, display1="none", display2="visible", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result, search_lower = search_lower, search_upper = search_upper, rpp=rpp)
        if lst3:
            result = ["Bhagavad Gita"]
            return render_template('home.html', lst3=lst3, display1="none", display2="none", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_lower = search_lower, search_upper = search_upper, rpp=rpp)

        flash('No Results')
        return redirect("/search")

    return render_template("search.html")


@app.route("/All", methods=["GET", "POST"])
def All():
    lst = cache.get("lst")
    lst2 = cache.get("lst2")
    lst3 = cache.get("lst3")
    search_lower = cache.get("search_lower")
    search_upper = cache.get("search_upper")

    rpp = request.form.get("rpp")
    try:
        rpp = int(float(rpp))
    except Exception as e:
        if rpp:
            flash('Please enter an integer.')
            if lst and lst2 and lst3:
                result = ["Bible", "Quran", "Bhagavad Gita"]
                return render_template('home.html', lst=lst, lst2=lst2, lst3=lst3, display1="visible", display2="visible", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=20)
            if lst and lst2:
                result = ["Bible", "Quran"]
                return render_template('home.html', lst=lst, lst2=lst2, display1="visible", display2="visible", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=20)
            if lst and lst3:
                result = ["Bible", "Bhagavad Gita"]
                return render_template('home.html', lst=lst, lst3=lst3, display1="visible", display2="none", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=20)
            if lst2 and lst3:
                result = ["Quran", "Bhagavad Gita"]
                return render_template('home.html', lst2=lst2, lst3=lst3, display1="none", display2="visible", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=20)
            if lst:
                result = ["Bible"]
                return render_template('home.html', lst=lst, display1="visible", display2="none", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=20)
            if lst2:
                result = ["Quran"]
                return render_template('home.html', lst2=lst2, display1="none", display2="visible", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=20)
            if lst3:
                result = ["Bhagavad Gita"]
                return render_template('home.html', lst3=lst3, display1="none", display2="none", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=20)

        if lst and lst2 and lst3:
                result = ["Bible", "Quran", "Bhagavad Gita"]
                return render_template('home.html', lst=lst, lst2=lst2, lst3=lst3, display1="visible", display2="visible", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=20)
        if lst and lst2:
                result = ["Bible", "Quran"]
                return render_template('home.html', lst=lst, lst2=lst2, display1="visible", display2="visible", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=20)
        if lst and lst3:
                result = ["Bible", "Bhagavad Gita"]
                return render_template('home.html', lst=lst, lst3=lst3, display1="visible", display2="none", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=20)
        if lst2 and lst3:
                result = ["Quran", "Bhagavad Gita"]
                return render_template('home.html', lst2=lst2, lst3=lst3, display1="none", display2="visible", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=20)
        if lst:
                result = ["Bible"]
                return render_template('home.html', lst=lst, display1="visible", display2="none", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=20)
        if lst2:
                result = ["Quran"]
                return render_template('home.html', lst2=lst2, display1="none", display2="visible", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=20)
        if lst3:
                result = ["Bhagavad Gita"]
                return render_template('home.html', lst3=lst3, display1="none", display2="none", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=20)

    if lst and lst2 and lst3:
        result = ["Bible", "Quran", "Bhagavad Gita"]
        return render_template('home.html', lst=lst, lst2=lst2, lst3=lst3, display1="visible", display2="visible", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=rpp)
    if lst and lst2:
        result = ["Bible", "Quran"]
        return render_template('home.html', lst=lst, lst2=lst2, display1="visible", display2="visible", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=rpp)
    if lst and lst3:
        result = ["Bible", "Bhagavad Gita"]
        return render_template('home.html', lst=lst, lst3=lst3, display1="visible", display2="none", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=rpp)
    if lst2 and lst3:
        result = ["Quran", "Bhagavad Gita"]
        return render_template('home.html', lst2=lst2, lst3=lst3, display1="none", display2="visible", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=rpp)
    if lst:
        result = ["Bible"]
        return render_template('home.html', lst=lst, display1="visible", display2="none", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=rpp)
    if lst2:
        result = ["Quran"]
        return render_template('home.html', lst2=lst2, display1="none", display2="visible", display3="none", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=rpp)
    if lst3:
        result = ["Bhagavad Gita"]
        return render_template('home.html', lst3=lst3, display1="none", display2="none", display3="visible", display_title="none", display_select="inline-block", display_img="none", result=result, search_upper=search_upper, search_lower=search_lower, rpp=rpp)


@app.route("/Bible", methods=["GET", "POST"])
def Bible():
    lst = cache.get("lst")
    lst2 = cache.get("lst2")
    lst3 = cache.get("lst3")
    search_lower = cache.get("search_lower")
    search_upper = cache.get("search_upper")

    if lst:
        result = ["Bible"]
    if lst2:
        result = ["Quran"]
    if lst3:
        result = ["Bhagavad Gita"]
    if lst and lst2:
        result = ["Bible", "Quran"]
    if lst and lst3:
        result = ["Bible", "Bhagavad Gita"]
    if lst2 and lst3:
        result = ["Quran", "Bhagavad Gita"]
    if lst and lst2 and lst3:
        result = ["Bible", "Quran", "Bhagavad Gita"]

    rpp = request.form.get("rpp")
    try:
        rpp = int(float(rpp))
    except Exception as e:
        if rpp:
            flash('Please enter an integer.')
            return render_template('Bible.html', lst=lst, result=result, search_upper=search_upper, search_lower=search_lower, rpp=20, rpp_v="none")
        return render_template('Bible.html', lst=lst, result=result, search_upper=search_upper, search_lower=search_lower, rpp=20, rpp_v="none")

    return render_template('Bible.html', lst=lst, result=result, search_upper=search_upper, search_lower=search_lower, rpp=rpp, rpp_v="none")

@app.route("/Quran", methods=["GET", "POST"])
def Quran():
    lst = cache.get("lst")
    lst2 = cache.get("lst2")
    lst3 = cache.get("lst3")
    search_lower = cache.get("search_lower")
    search_upper = cache.get("search_upper")

    if lst:
        result = ["Bible"]
    if lst2:
        result = ["Quran"]
    if lst3:
        result = ["Bhagavad Gita"]
    if lst and lst2:
        result = ["Bible", "Quran"]
    if lst and lst3:
        result = ["Bible", "Bhagavad Gita"]
    if lst2 and lst3:
        result = ["Quran", "Bhagavad Gita"]
    if lst and lst2 and lst3:
        result = ["Bible", "Quran", "Bhagavad Gita"]

    rpp = request.form.get("rpp")
    try:
        rpp = int(float(rpp))
    except Exception as e:
        if rpp:
            flash('Please enter an integer.')
            return render_template('Quran.html', lst2=lst2, result=result, search_upper=search_upper, search_lower=search_lower, rpp=20, rpp_v="none")
        return render_template('Quran.html', lst2=lst2, result=result, search_upper=search_upper, search_lower=search_lower, rpp=20, rpp_v="none")

    return render_template('Quran.html', lst2=lst2, result=result, search_upper=search_upper, search_lower=search_lower, rpp=rpp, rpp_v="none")

@app.route("/Bhagavad", methods=["GET", "POST"])
def Bhagavad():
    lst = cache.get("lst")
    lst2 = cache.get("lst2")
    lst3 = cache.get("lst3")
    search_lower = cache.get("search_lower")
    search_upper = cache.get("search_upper")

    if lst:
        result = ["Bible"]
    if lst2:
        result = ["Quran"]
    if lst3:
        result = ["Bhagavad Gita"]
    if lst and lst2:
        result = ["Bible", "Quran"]
    if lst and lst3:
        result = ["Bible", "Bhagavad Gita"]
    if lst2 and lst3:
        result = ["Quran", "Bhagavad Gita"]
    if lst and lst2 and lst3:
        result = ["Bible", "Quran", "Bhagavad Gita"]

    rpp = request.form.get("rpp")
    try:
        rpp = int(float(rpp))
    except Exception as e:
        if rpp:
            flash('Please enter an integer.')
            return render_template('Bhagavad.html', lst3=lst3, result=result, search_upper=search_upper, search_lower=search_lower, rpp=20, rpp_v="none")
        return render_template('Bhagavad.html', lst3=lst3, result=result, search_upper=search_upper, search_lower=search_lower, rpp=20, rpp_v="none")

    return render_template('Bhagavad.html', lst3=lst3, result=result, search_upper=search_upper, search_lower=search_lower, rpp=rpp, rpp_v="none")

@app.route("/verse", methods=["GET", "POST"])
def verse():
    
    if request.method == "POST":
        rpp = request.form.get("rpp")
        try:
            rpp = int(float(rpp))
        except Exception as e:
            rpp = 20
        rpp = 20
        print(rpp)

        bible_name = request.form.get("bible_name")
        bible_chapter = request.form.get("bible_chapter")
        bible_verse = request.form.get("bible_verse")
        bible_name = bible_name.title()
        cache.set("bible_name", bible_name)
        cache.set("bible_chapter", bible_chapter)
        cache.set("bible_verse", bible_verse)

        quran_sura = request.form.get("quran_sura")
        quran_verse = request.form.get("quran_verse")
        cache.set("quran_sura", quran_sura)
        cache.set("quran_verse", quran_verse)

        hindu_chapter = request.form.get("hindu_chapter")
        hindu_verse = request.form.get("hindu_verse")
        cache.set("hindu_chapter", hindu_chapter)
        cache.set("hindu_verse", hindu_verse)

        bible_name = cache.get("bible_name")
        bible_chapter = cache.get("bible_chapter")
        bible_verse = cache.get("bible_verse")

        if bible_name and bible_chapter and bible_verse:
            lst = db1.execute("SELECT * FROM verses WHERE book_name == ? AND chapter == ? AND verse == ?", bible_name, bible_chapter, bible_verse,)
            if not lst:
                flash('Please enter a valid query.')
                return redirect("/verse")
            return render_template('Bible.html', lst=lst, display_select="none", search_upper="", search_lower="", rpp=rpp, rpp_search="none")

        if bible_name and bible_verse and not bible_chapter:
            flash('Please enter a valid query.')
            return redirect("/verse")

        if bible_name and bible_chapter:
            lst = db1.execute("SELECT * FROM verses WHERE book_name == ? AND chapter == ?", bible_name, bible_chapter)
            if not lst:
                flash('Please enter a valid query.')
                return redirect("/verse")
            return render_template('Bible.html', lst=lst, display_select="none", search_upper="", search_lower="", rpp=rpp, rpp_search="none")

        if bible_name:
            lst = db1.execute("SELECT * FROM verses WHERE book_name == ?", bible_name)
            if not lst:
                flash('Please enter a valid query.')
                return redirect("/verse")
            return render_template('Bible.html', lst=lst, display_select="none", search_upper="", search_lower="", rpp=rpp, rpp_search="none")

        # Quran
        quran_sura = cache.get("quran_sura")
        quran_verse = cache.get("quran_verse")

        if quran_sura and quran_verse:
            lst2 = db2.execute("SELECT * FROM verses WHERE sura == ? AND verse == ?", quran_sura, quran_verse)
            if not lst2:
                flash('Please enter a valid query.')
                return redirect("/verse")
            return render_template('Quran.html', lst2=lst2, display_select="none", search_upper="", search_lower="", rpp=rpp, rpp_search="none")

        if quran_sura:
            lst2 = db2.execute("SELECT * FROM verses WHERE sura == ?", quran_sura)
            if not lst2:
                flash('Please enter a valid query.')
                return redirect("/verse")
            return render_template('Quran.html', lst2=lst2, display_select="none", search_upper="", search_lower="", rpp=rpp, rpp_search="none")

        # Bhagavad Gita
        hindu_chapter = cache.get("hindu_chapter")
        hindu_verse = cache.get("hindu_verse")

        if hindu_chapter and hindu_verse:
            lst3 = db3.execute("SELECT * FROM verses WHERE Chapter == ? AND Verse == ?", hindu_chapter, hindu_verse)
            if not lst3:
                flash('Please enter a valid query.')
                return redirect("/verse")
            return render_template('Bhagavad.html', lst3=lst3, display_select="none", search_upper="", search_lower="", rpp=rpp, rpp_search="none")

        if hindu_chapter:
            lst3 = db3.execute("SELECT * FROM verses WHERE Chapter == ?", hindu_chapter)
            if not lst3:
                flash('Please enter a valid query.')
                return redirect("/verse")
            return render_template('Bhagavad.html', lst3=lst3, display_select="none", search_upper="", search_lower="", rpp=rpp, rpp_search="none")

        flash('Please enter a valid query.')
        return redirect("/verse")

    return render_template("verse.html")