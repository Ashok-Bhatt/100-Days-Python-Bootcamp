from flask import Flask
from time import sleep

app = Flask(__name__)
""" 
print(__name__)         # __main__
 """

def make_bold(func):
    def wrapper():
        return "<b>" + func() + "</b>"
    return wrapper

def make_emphasis(func):
    def wrapper():
        return "<i>" + func() + "</i>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper

@app.route("/")
def hello_world():
    return "Ya hego tumharo pehlo flask website, so chillax!"

@app.route("/home")
@make_bold
@make_emphasis
@make_underlined
def home():
    return "You are home!"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Welcome {name}, your age is {number}."

@app.route("/<path:name>")
def greeting(name):
    return f"Welcome {name}"

@app.route("/new")
def display_page():
    sleep(1)
    return '<h1 style="text-align:center">My Image</h1>' \
            '<p>Required paragraph</p>' \
            '<img src="https://media.giphy.com/media/Qv7WFppXtkqkM/giphy.gif" width="200px" border="5px solid #000">'

if __name__ == "__main__":
    app.run(debug=True)

# Mac command to run flask application: export FLASK_APP=basic_flask_application.py
# Window command to run flask application: set FLASK_APP=basic_flask_application.py
# next command: flask run
# To exit: CTRL + C