#!/usr/bin/python3
""" a script to start a flask web app"""


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=false)
def hbnb():
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def hbnb_c(text):
    return f"C {text.replace('_', ' ')}"

@app.route("/python/<text>", strict_slashes=False)
def hbnb_python(text="is_cool"):
    return f"Python {text.replace('_', ' ')}"

@app.route("/number/<int:n>", strict_slashes=False)
def hbnb_number(n):
    return "n is a number"

@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', number=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def odd_or_even(n):
    return render_template('6-number_odd_or_even.html', number=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
