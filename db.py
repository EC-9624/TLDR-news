import json
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()


def insertdb():
    print("connecting to db...")
    client = MongoClient(os.getenv("MONGO_URL"))
    print("db conected!")

    # Get the database and collection
    db = client["TLDRnews"]
    collection = db["news"]
    print("inserting....")
    # using json file to insert because of token limitation
    f = open('data.json')
    data = json.load(f)

    for d in data:
        exists = collection.find_one({"link": d["link"]})

        if not exists:
            collection.insert_one(d)
    print("Finished!")


insertdb()
