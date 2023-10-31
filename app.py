from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return "HEllo there from Flask"

@app.route("/dog")
def dog():
    hello = 'woof woof'
    return hello


if __name__ == "__main__":
    app.run(debug=True)
