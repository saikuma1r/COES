from flask import Blueprint,render_template
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64

views = Blueprint('views',__name__)
@views.route('/')
def home():
    return render_template('home.html')

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
    data = sns.load_dataset("iris")
    iris_data = sns.load_dataset("iris")
    print(iris_data.head())
    sns_plot = sns.pairplot(data, hue='species')

    # Save the plot to a BytesIO object
    img = io.BytesIO()
    sns_plot.savefig(img, format='png')
    img.seek(0)

    # Encode the plot in base64 to display in HTML
    plot_url = base64.b64encode(img.getvalue()).decode()
    return render_template("visual.html", plot_url=plot_url)
