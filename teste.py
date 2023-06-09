import json
import os

path = os.path.join(os.getcwd(), "dados.json")
with open(path) as data:
    payload = json.load(data)
    for data in payload:
        if data["type"] == 1 and data["subType"] == 0:
            print(data)

