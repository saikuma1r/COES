from flask import Blueprint,render_template

views = Blueprint('views',__name__)
@views.route('/')
def home():
    return render_template("home.html")
@views.route('/about')
def about():
    return render_template("about.html")

@views.route('/insites')
def insites():
    return render_template("insites.html")

@views.route('/contact')
def contact():
    return render_template("contact.html")

@views.route('/data_load')
def visual():
    return render_template("visual.html")
