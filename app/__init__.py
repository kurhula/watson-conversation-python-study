import ConfigParser
import os
from flask import Flask

app = Flask(__name__, template_folder="views")

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'config.cfg'))

# Registering Blueprints
from app.controllers import scores
from app.controllers import home
from app.controllers import messages

app.register_blueprint(scores.module)
app.register_blueprint(home.module)
app.register_blueprint(messages.module)
