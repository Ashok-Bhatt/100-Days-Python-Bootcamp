from flask import Flask, render_template
from random import randint
from datetime import datetime
import requests

app = Flask(__name__)


@app.route("/")
def displayHome():
    return render_template("index.html", rand_num = randint(1,10), current_year=datetime.today().year)


@app.route("/about/<name>")
def showAbout(name):
    gender_response =  requests.get(f"https://api.genderize.io?name={name.title()}").json()
    age_response = requests.get(f"https://api.agify.io?name={name}").json()
    return render_template("about.html", name=name, gender=gender_response["gender"], age=age_response["age"])


@app.route("/blog/<num>")
def showBlogs(num):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_blogs = response.json()
    return render_template("blog.html", blogs=all_blogs)


if __name__=="__main__":
    app.run(debug=True)