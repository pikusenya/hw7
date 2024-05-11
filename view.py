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


@app.route("/text_editor", methods=["POST"])
def text_editor():
    data = request.json
    return controller.text_editor(data)

@app.route("/parser", methods=["POST"])
def parser():
    data = request.json
    return controller.parser(data)

if __name__ == "__main__":
    app.run(debug=True)
