import json
from random import randint

from flask import Flask, render_template, request
from flask.json import jsonify

from backend.user import user

app = Flask(__name__,
            static_folder = "./dist/static",
            template_folder = "./dist")

app.register_blueprint(user, url_prefix='/user')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template("index.html")


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run()