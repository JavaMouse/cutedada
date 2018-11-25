from random import randint

from flask import Flask, render_template, request
from flask.json import jsonify

from backend.controller.TableController import table
from backend.controller.test import test
from backend.controller.UserController import user

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(test, url_prefix='/test')
app.register_blueprint(table, url_prefix='/table')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")


if __name__ == '__main__':
    app.config['JSON_AS_ASCII'] = False
    app.config['SECRET_KEY'] = 'chennan is a girl'
    app.run(debug=True)