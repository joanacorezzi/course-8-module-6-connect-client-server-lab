from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# in-memory list of events
events = [
    {"id": 1, "title": "Yoga in the Park"},
    {"id": 2, "title": "Lake 5K Run"}
]

# GET / -> return a welcome message
@app.route("/", methods=["GET"])
def welcome():
    # return JSON with a "message" key
    return jsonify({"message": "Welcome!"}), 200


# GET /events -> return all events as JSON
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200


# POST /events -> add a new event
@app.route("/events", methods=["POST"])
def add_event():
    # get JSON data from the request body
    data = request.get_json() or {}

    # basic validation: make sure "title" exists
    # tests expect 400 or 422 when data is missing
    if "title" not in data or not data["title"]:
        return jsonify({"error": "Title is required"}), 400

    # compute next id (max existing id + 1)
    new_id = max((e["id"] for e in events), default=0) + 1

    # create the new event
    new_event = {"id": new_id, "title": data["title"]}

    # add it to the list
    events.append(new_event)

    # return the new event with status 201 
    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True)
