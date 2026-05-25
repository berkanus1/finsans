import csv
import io
import json
import os

from flask import Flask, redirect, render_template, request, Response, url_for

app = Flask(__name__)
DATA_FILE = "data.json"


def load():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save(transactions):
    with open(DATA_FILE, "w") as f:
        json.dump(transactions, f, indent=2)


@app.route("/")
def index():
    transactions = load()
    balance = sum(t["amount"] for t in transactions)
    return render_template("index.html", transactions=transactions, balance=balance)


@app.route("/add", methods=["POST"])
def add():
    transactions = load()
    try:
        amount = float(request.form["amount"])
        category = request.form["category"].strip() or "other"
        note = request.form["note"].strip()
        kind = request.form["kind"]
        if kind == "expense":
            amount = -abs(amount)
        else:
            amount = abs(amount)
        transactions.append({"amount": amount, "category": category, "note": note, "type": kind})
        save(transactions)
    except (ValueError, KeyError):
        pass
    return redirect(url_for("index"))


@app.route("/export")
def export():
    transactions = load()
    output = io.StringIO()
    writer = csv.DictWriter(output, fieldnames=["type", "amount", "category", "note"])
    writer.writeheader()
    writer.writerows(transactions)
    csv_data = "﻿" + output.getvalue()
    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment; filename=transactions.csv"},
    )


if __name__ == "__main__":
    app.run(debug=True)
