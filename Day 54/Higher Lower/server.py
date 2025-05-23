from flask import Flask
from random import randint

app = Flask(__name__)
rand_num = randint(0,9)

@app.route("/")
def showHome():
    return "<h1 style='text-align: center'>Guess a number between 0 and 9</h1>" \
    "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' width='200px'></img>"

@app.route("/<int:number>")
def showresult(number):
    if number > rand_num:
        return "<h1 style='color:violet'>Too high, try again!</h1>" \
        "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' width='200px'></img>"
    elif number < rand_num:
        return "<h1 style='color:red'>Too low, try again!</h1>" \
        "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' width='200px'></img>"
    else:
        return "<h1 style='color:green'>You found me!!</h1>" \
        "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' width='200px'></img>"

if __name__ == "__main__":
    app.run(debug=True)