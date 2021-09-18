from flask import Blueprint, render_template


views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", var=3)

@views.route("/about/")
def about():
    return render_template("index.html", var = "hello")
