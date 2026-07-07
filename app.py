"""example-app — a tiny JSON service."""
import subprocess
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
    # BUG (test gate): missing comma and exclamation — tests expect "Hello, world!"
    return jsonify(message=f"{greeting} {name}")


@app.route("/uppercase")
def uppercase():
    text = request.args.get("text", "")
    # BUG (code-review gate): endpoint is /uppercase but lowercases the input
    return jsonify(result=text.lower())


@app.route("/lookup")
def lookup():
    host = request.args.get("host", "localhost")
    # BUG (security gate): shell=True on user input — command injection
    out = subprocess.check_output(f"nslookup {host}", shell=True)
    return out
