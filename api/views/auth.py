from flask import Blueprint, jsonify, abort, request, make_response, json
from api.models.products import Product, my_products
#from api.controllers.validators import is_valid

appblueprint = Blueprint('api',__name__)

@appblueprint.route('/')
def welcomeMessage():
    return "<h1>Welcome to Store Manager.</h1>"
