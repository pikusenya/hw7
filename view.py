from flask import Flask, request
from controller import controller

app = Flask("test_prjct")

@app.route("/")
def start():
    return "this is test prjct"

@app.route("/calculation", methods=["POST"])
def calculation():
    data = request.json
    return controller.calculate(data)


# @app.route("/text_redactor", methods=["POST"])


# @app.route("/parser", methods=["POST"])

if __name__ == "__main__":
    app.run(debug=True)
