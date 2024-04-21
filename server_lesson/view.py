
from flask import Flask, render_template, redirect, url_for, request
from controller import controller

app = Flask("test_pj")


@app.route("/")
def hello():
    return "Hello!"


@app.route("/hello_test/123", methods=["POST"])
def hello_test_123():
    return render_template("test.html")


@app.route("/redirect_url")
def redirect_url():
    return redirect(url_for("hello_test"))


@app.route("/test_post", methods=["POST"])
def test_post():
    print(request.json)
    return "response"


@app.route("/mvc_example", methods=["GET"])
def mvc_example():
    respone = controller.get_json_data()
    return respone


@app.route("/sum", methods=["POST"])
def sum():
    a = request.json["a"]
    b = request.json["b"]
    response = controller.sum(a, b)
    return str(response)


if __name__ == "__main__":
    app.run(debug=True)
