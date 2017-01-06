from flask import render_template, flash, redirect, request
from app import app
from app import watson


@app.route('/')
@app.route('/index')
def index():
    return render_template("home/index.html")

@app.route('/api/message', methods=["GET","POST"])
def message():
    json = request.get_json(force=True)
    text = watson.sendMessage(json["id"], json["message"])
    return text
