# Import libraries for Flask, MongoDB, and CORS
from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
import os

app = Flask(__name__)  # Create Flask app instance
CORS(app)  # Enable CORS for cross-origin requests

# MongoDB URI for CycleWorks database connection
mongo_uri = "mongodb+srv://cycleworks:Cycle123!@cycleworksdb.kqjx3hd.mongodb.net/?retryWrites=true&w=majority&appName=CycleWorksDB"
client = MongoClient(mongo_uri)  # Connect to MongoDB
db = client["cycleworks"]  # Select database
bikes_collection = db["bikes"]  # Select bikes collection

# GET route to fetch all bikes
@app.route("/bikes", methods=["GET"])
def get_bikes():
    bikes = list(bikes_collection.find({}, {"_id": 0}))  # Retrieve bikes, exclude '_id'
    return jsonify(bikes)  # Return as JSON

# POST route to add a new bike
@app.route("/bikes", methods=["POST"])
def add_bike():
    data = request.get_json()  # Parse incoming JSON data
    name = data.get("name")  # Extract bike name
    price = float(data.get("price"))  # Extract and convert price
    condition = data.get("condition")  # Extract condition
    bike = {"name": name, "price": price, "condition": condition}  # Create bike object
    bikes_collection.insert_one(bike)  # Insert into database
    return jsonify({"message": "Bike added", "bike": bike}), 201  # Return success response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Run app on port 5000