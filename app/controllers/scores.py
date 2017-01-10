import json
from flask import Blueprint, render_template, flash, redirect, request
from app import app
from app.data import score_repository
from bson import json_util

module = Blueprint('score', __name__, url_prefix='/api/score')

@module.route('/', methods=["POST"])
def score():
    jsonRequest = request.get_json(force=True)
    score_repository.addScore(jsonRequest["inputText"], jsonRequest["message"], jsonRequest["intents"], jsonRequest["entities"], jsonRequest["score"])
    return "OK"

@module.route('/', methods=["GET"])
def scoreList():
    scores = score_repository.listScores()
    return json.dumps(scores, default=json_util.default)