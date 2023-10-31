import openai
from flask import Flask, render_template, request
from dotenv import dotenv_values

config = dotenv_values(".env")

app = Flask(__name__, template_folder="templates")
openai.api_key = config["OPENAI_KEY"]


@app.route("/palette", methods=["POST"])
def prompt_to_palette():
    print("sarples")
    app.logger.info(request.form.get("query"))
    app.logger.info("GIT THE ROUTE")
    # return "Reached route!"


@app.route("/")
def index():
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct", prompt="Give me a funny word"
    )
    print(response["choices"][0]["text"])
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
