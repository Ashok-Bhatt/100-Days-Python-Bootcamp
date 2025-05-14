
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def displayHome():
    return render_template("index.html")

@app.route("/login", methods=["post"])
def login():
    name = request.form["name"]
    password = request.form["password"]
    return f"<h1>Name: {name}, Password: {password}</h1>"

if __name__ == "__main__":
    app.run(debug=True)