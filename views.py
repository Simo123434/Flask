from flask import Blueprint, render_template, request
import sys



views = Blueprint(__name__, "views")

@views.route("/", methods=["GET", "POST"])
def home():
    return render_template("index.html", var=3) #define variables in this line that can be used in html

@views.route("/about/")
def about():
    print("Welcome", file=sys.stdout) #printing to python console
    return render_template("index.html", var = "hello")

@views.route("/buttons/", methods=["GET", "POST"])
def clicked():
    if request.method == 'POST':
        if request.form.get('Button1') == 'B1clicked':
            print("You clicked", file=sys.stdout)

        else:
            return 'hi'
    return render_template("button.html")

