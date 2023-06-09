from flask import Blueprint, jsonify, make_response
import json
import os

cat_bp = Blueprint(__name__, "cat_bp")


@cat_bp.route("/<string:type>/<string:subType>")
def index(type, subType):
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

