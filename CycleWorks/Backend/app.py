from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

mongo_uri = os.getenv("MONGODB_URI", "mongodb+srv://cycleworks:Cycle123!@cluster0.abc123.mongodb.net/?retryWrites=true&w=majority")
client = MongoClient(mongo_uri)
db = client["cycleworks"]
bikes_collection = db["bikes"]

@app.route("/bikes", methods=["GET"])
def get_bikes():
    bikes = list(bikes_collection.find({}, {"_id": 0}))
    return jsonify(bikes)

@app.route("/bikes", methods=["POST"])
def add_bike():
    data = request.get_json()
    name = data.get("name")
    price = float(data.get("price"))
    condition = data.get("condition")
    bike = {"name": name, "price": price, "condition": condition}
    bikes_collection.insert_one(bike)
    return jsonify({"message": "Bike added", "bike": bike}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)