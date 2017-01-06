import ConfigParser
import os
from flask import Flask

app = Flask(__name__)

config = ConfigParser.ConfigParser()
config.read(os.path.join(os.path.abspath(os.path.dirname(__file__)),'config.cfg'))

from app import views