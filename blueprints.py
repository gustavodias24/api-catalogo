from flask import Blueprint, jsonify, make_response
import json
import os

cat_bp = Blueprint("cat_bp", __name__)


@cat_bp.route("/")
def index():
    return jsonify({"msg": "Deus é fiél."})
@cat_bp.route("/<string:type>/<string:subType>")
def get(type, subType):
    path = os.path.join(os.getcwd(), "dados.json")
    with open(path) as data:
        payload = json.load(data)
        for data in payload:
            if data["type"] == int(type) and data["subType"] == int(subType):
                return jsonify(data)

        return make_response(
            jsonify({"error": True, "type": type, "subType": subType}),
            400
        )

