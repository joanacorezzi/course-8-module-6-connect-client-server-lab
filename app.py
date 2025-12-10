
from flask import Flask, request, jsonify

# create the Flask application
app = Flask(__name__)

# in-memory list of events 
events = [
    {"id": 1, "title": "Yoga in the Park"},
    {"id": 2, "title": "Lake 5K Run"}
]

# GET /  -> return a simple welcome message in JSON
@app.route("/", methods=["GET"])
def welcome():
    # jsonify turns the Python dict into JSON
    return jsonify({"message": "Welcome!"}), 200


# GET /events  -> return all events as JSON
@app.route("/events", methods=["GET"])
def get_events():
    # return the whole list of events
    return jsonify(events), 200


# POST /events  -> accept JSON with a new event and store it
@app.route("/events", methods=["POST"])
def add_event():
    # get JSON data from the request body
    # expected format: { "title": "Some event title" }
    data = request.get_json()

    # find the next id: take the max existing id and add 1
    # default=0 in case the list is empty
    new_id = max((e["id"] for e in events), default=0) + 1

    # create a new event dictionary
    new_event = {"id": new_id, "title": data["title"]}

    # add the new event to in-memory list
    events.append(new_event)

    # return the new event with status code 201 
    return jsonify(new_event), 201



if __name__ == "__main__":
    app.run(debug=True)
