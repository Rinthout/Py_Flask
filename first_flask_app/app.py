from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Dit is een test: Hello, World!</p>"