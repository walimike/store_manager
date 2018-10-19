from flask import Flask

app = Flask(__name__)

from api.views.auth import appblueprint

app.register_blueprint(views.auth.appblueprint, url_prefix = '/v1/api/')
