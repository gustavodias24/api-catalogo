from decouple import config
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://{}:{}@cluterb.ypmgnks.mongodb.net/?retryWrites=true&w=majority"
    .format(config("USER"), config("PASS"))
)

db = client["catalogoDB"]
col = db["produtos"]

print(col.find_one({"type": 0, "subType": 1}))
