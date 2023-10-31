import openai
from flask import Flask, render_template, request
from dotenv import dotenv_values
import json


config = dotenv_values(".env")

app = Flask(__name__, template_folder="templates")
openai.api_key = config["OPENAI_KEY"]


def get_colors(msg):
    prompt = f"""
    Q: oncvert the following verbal description of a color palette into a list of colors: sage, nature, earth
    A: ["#EDF1D6", "#609966", "#40513B"]

    Desired Format: a JSON array of hexadecimal color codes

    Q: Convert the following verbal description of a color palette into a list of colors: {msg}
    A: 
    """
    response = openai.Completion.create(
        prompt=prompt, model="gpt-3.5-turbo-instruct", max_tokens=200
    )

    colors = json.loads(response["choices"][0]["text"])
    return colors


@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    query = request.form.get("query")
    colors = get_colors(query)
    return {"colors": colors}


@app.route("/")
def index():
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct", prompt="Give me a funny word"
    )
    print(response["choices"][0]["text"])
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
