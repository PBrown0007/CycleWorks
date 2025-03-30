from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["cycleworks"]
bikes_collection = db["bikes"]

@app.route("/bikes", methods=["GET"])
def get_bikes():
    bikes = list(bikes_collection.find({}, {"_id": 0}))  # Exclude _id from results
    return jsonify(bikes)

@app.route("/bikes", methods=["POST"])
def add_bike():
    data = request.get_json()
    name = data.get("name")
    price = float(data.get("price"))
    condition = data.get("condition")
    bike = {"name": name, "price": price, "condition": condition}
    result = bikes_collection.insert_one(bike)
    bike["_id"] = str(result.inserted_id)  # Convert ObjectId to string
    return jsonify({"message": "Bike added", "bike": bike}), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")