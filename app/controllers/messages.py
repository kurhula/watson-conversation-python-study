import json
from flask import Blueprint, render_template, request
from app.services import watson_service
from bson import json_util

module = Blueprint('messages', __name__, url_prefix='/api/message')


@module.route('/', methods=["POST"])
def message():
    jsonRequest = request.get_json(force=True)
    text = watson.sendMessage(jsonRequest["id"], jsonRequest["message"])
    return json.dumps(text)
