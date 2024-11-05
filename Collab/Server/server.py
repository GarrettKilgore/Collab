from flask import Flask, request
from RockClimbing import RockClimbingDB

app = Flask(__name__)

@app.route("/rockclimbing/<int:climbing_id>", methods=["OPTIONS"])
def handle_cors_options(climbing_id):
    return "", 204, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Method": "PUT, DELETE",
        "Access-Control-Allow-Headers": "Content-Type"
    }

@app.route("/rockclimbing", methods=["GET"])
def retrieve_review():
    db = RockClimbingDB("rockclimbing_db.db")
    rockclimbing = db.getRockClimbings()
    return rockclimbing, 200, {"Access-Control-Allow-Origin" : "*"}

@app.route("/rockclimbing", methods=["POST"])
def createRockClimbing():
    print("The requet data is: ", request.form)
    name = request.form["name"]
    review = request.form["review"]
    rating = request.form["rating"]
    db = RockClimbingDB("rockclimbing_db.db")
    db.createRockClimbing(name,review,rating)
    return "Created", 201, {"Access-Control-Allow-Origin" : "*"}

@app.route("/rockclimbings/<int:climbing_id>", methods=["PUT"])
def update_rockclimbing(climbing_id):
    print("update climbing with ID", climbing_id)
    db = RockClimbingDB("rockclimbing_db.db")
    rockclimbing = db.getRockClimbing(climbing_id)
    if rockclimbing:
        name = request.form["name"]
        review = request.form["review"]
        rating = request.form["rating"]
        db = RockClimbingDB("rockclimbing_db.db")
        db.updateRockClimbging(climbing_id,name,review,rating)
        return "Update", 200, {"Access_Control_Allow_Origin" : "*"}
    else:
        return f"Rock climbing with {climbing_id} not found", 404, {"Access_Control_Allow_Origin" : "*"}

def run():
    app.run(port=8080, host='0.0.0.0')

if __name__=="__main__":
    run()