from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
api = Blueprint('api', __name__)

@api.route('/test-private')
@jwt_required()
def test():
    return jsonify({"msg": "Testing Private API Routes"}), 200
