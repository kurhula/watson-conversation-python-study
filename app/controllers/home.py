from flask import Blueprint, render_template

module = Blueprint('home', __name__, url_prefix='/')

@module.route('/')
@module.route('/index')
def index():
    return render_template("home/index.html")