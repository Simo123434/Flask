from flask import Blueprint, render_template


views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", var=3) #define variables in this line that can be used in html

@views.route("/about/")
def about():
    return render_template("index.html", var = "hello")
