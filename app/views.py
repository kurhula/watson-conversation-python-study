from flask import render_template, flash, redirect, request
import json
from app import app
from app import watson
from app import db
from bson import json_util

@app.route('/')
@app.route('/index')
def index():
    return render_template("home/index.html")

@app.route('/api/message', methods=["POST"])
def message():
    jsonRequest = request.get_json(force=True)
    text = watson.sendMessage(jsonRequest["id"], jsonRequest["message"])
    return json.dumps(text)

@app.route('/api/score', methods=["POST"])
def score():
    jsonRequest = request.get_json(force=True)
    db.addScore(jsonRequest["inputText"], jsonRequest["message"], jsonRequest["intents"], jsonRequest["entities"], jsonRequest["score"])
    return "OK"

@app.route('/api/score', methods=["GET"])
def scoreList():
    scores = db.listScores()
    return json.dumps(scores, default=json_util.default)