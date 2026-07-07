"""example-app — a tiny JSON service."""
from flask import Flask, jsonify, request

app = Flask(__name__)

GREETINGS = {
    "en": "Hello",
    "es": "Hola",
    "fr": "Bonjour",
    "de": "Hallo",
}


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/greet")
def greet():
    lang = request.args.get("lang", "en")
    name = request.args.get("name", "world")
    greeting = GREETINGS.get(lang, GREETINGS["en"])
    return jsonify(message=f"{greeting}, {name}!")
