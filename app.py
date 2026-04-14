from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import json
import os

app = Flask(__name__)

STORAGE_PATH = os.path.join("storage", "data.json")


def read_data():
    """Читаем данные из data.json"""
    with open(STORAGE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def write_data(data):
    """Записываем данные в data.json"""
    with open(STORAGE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


# ── Маршруты ──────────────────────────────────────────────

@app.route("/")
def index():
    return render_template("index.html", active_page="home", title="Home")


@app.route("/message")
def message_page():
    return render_template("message.html", active_page="message", title="Send message")


@app.route("/message", methods=["POST"])
def message():
    username = request.form.get("username", "")
    message  = request.form.get("message", "")

    # Ключ — текущее время
    key = str(datetime.now())

    data = read_data()
    data[key] = {"username": username, "message": message}
    write_data(data)

    return redirect(url_for("index"))


@app.route("/read")
def read():
    data = read_data()
    return render_template("read.html", messages=data, active_page="read", title="Read messages")


# ── Обработчик 404 ────────────────────────────────────────

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", title="404 - Page Not Found"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
