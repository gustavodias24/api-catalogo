from flask import Blueprint, jsonify, make_response, request
from pymongo import MongoClient
from decouple import config
import requests

uri_db = "mongodb+srv://{}:{}@cluterb.ypmgnks.mongodb.net/?retryWrites=true&w=majority".format(
    config("USER"), config("PASS")
)

client = MongoClient(
    "mongodb+srv://benicio:233281@cluterb.ypmgnks.mongodb.net/?retryWrites=true&w=majority"
)

db = client["catalogoDB"]
col_produtos = db["produtos"]
col_pedidos = db["pedidos"]

cat_bp = Blueprint("cat_bp", __name__)


@cat_bp.route("/")
def index():
    return jsonify({"msg": "Deus é fiél."})


@cat_bp.route("/<int:t>/<int:subType>")
def get(t, subType):
    result = col_produtos.find_one(
        {
            "type": t,
            "subType": subType
        }
    )

    if result is not None:
        return jsonify(result)
    else:
        return make_response(
            jsonify({"error": True, "type": t, "subType": subType, "result": result}),
            400
        )


@cat_bp.route("/myWebHook", methods=["POST"])
def verify_payers():
    token_acess = config("TOKEN_MP")

    payload = request.get_json()

    id = payload["data"]["id"]

    base = "https://api.mercadopago.com"
    headers = {
        "Authorization": "Bearer " + token_acess
    }

    resp = requests.get("{}/v1/payments/{}".format(base, id), headers=headers)

    col_pedidos.update_one(
        {
            "_id": id
        },
        {
            '$set': {
                'status': resp.json()["status"]
            }
        }
    )

    return make_response(jsonify({"msg": "ok"}), 200)


@cat_bp.route("/salvarPedido", methods=["POST"])
def save_orde():
    payload = request.get_json()

    col_pedidos.insert_one(payload)

    return jsonify(payload)
