from flask import Blueprint, jsonify, abort, request, make_response, json
from api.models.products import Product, my_products
from api.controllers.validators import is_valid

appblueprint = Blueprint('api',__name__)

@appblueprint.route('/')
def welcomeMessage():
    return "<h1>Welcome to Store Manager.</h1>"

@appblueprint.route('/products', methods=['GET'])
def view_products():
    if not is_valid.empty_list():
        return jsonify({"Message":"Product list is currently empty"}), 200
    return jsonify({"Product list":my_products.product_list}), 200
