from flask import Flask, request
from RockClimbing import RockClimbingDB
from passlib.hash import bcrypt

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
    #print("The requested data is: ", request.form)
    
    Name = request.form["Name"]
    Difficulty = request.form["Difficulty"]
    Color = request.form["Color"]
    Height = request.form["Height"]
    TypeofHold = request.form["TypeofHold"]
    Rope = request.form["Rope"]
    Review = request.form["Review"]
    #print("The review is" + Review)
    db = RockClimbingDB("rockclimbing_db.db")
    db.createRockClimbing(Name,Difficulty,Color,Height,TypeofHold,Rope,Review)
    return "Created", 201, {"Access-Control-Allow-Origin" : "*"}

@app.route("/rockclimbing/<int:climbing_id>", methods=["PUT"])
def updateRockClimbing(climbing_id):
    print("update climbing with ID", climbing_id)
    db = RockClimbingDB("rockclimbing_db.db")
    rockclimbing = db.getRockClimbing(climbing_id)
    if rockclimbing:
        Name = request.form["Name"]
        Difficulty = request.form["Difficulty"]
        Color = request.form["Color"]
        Height = request.form["Height"]
        TypeofHold = request.form["TypeofHold"]
        Rope = request.form["Rope"]
        Review = request.form["Review"]
        db = RockClimbingDB("rockclimbing_db.db")
        db.updateRockClimbing(climbing_id,Name,Difficulty,Color,Height,TypeofHold,Rope,Review)
        return "Update", 200, {"Access-Control-Allow-Origin" : "*"}
    else:
        return f"Rock climbing with {climbing_id} not found", 404, {"Access-Control-Allow-Origin" : "*"}
'''    
@app.route("/users", methods=["POST"])
def create():
    print("The request data is: ", request.form)
    #extract email and password from the request.form
    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    email = request.form['email']
    password = request.form['password']
    #create a new DB thread
    db = RockClimbingDB("rockclimbing_db.db")
    #try to get the user info from DB using email
    user = db.get_user_by_email(email)
    #if user
    if user:
        #return a massage and 201 status
            return "Authendicated", 201, {"Access-Control-Allow-Origin": "*"}
        #otherwise
        else:
            return "Unauthorized", 401, {"Access-Control-Allow-Origin": "*"}
    #else return a a message and 401 status
    return "Unauthorized", 401, {"Access-Control-Allow-Origin": "*"}

@app.route("/session/auth", methods=["POST"])
def login():
    print("The request data is: ", request.form)
    #extract email and password from the request.form
    email = request.form['email']
    password = request.form['password']
    #create a new DB thread
    db = RockClimbingDB("rockclimbing_db.db")
    #try to get the user info from DB using email
    user = db.get_user_by_email(email)
    #if user
    if user:
        #check if password matches
        if bcrypt.verify(password, user["password"]):
            #return a massage and 201 status
            return "Authendicated", 201, {"Access-Control-Allow-Origin": "*"}
        #otherwise
        else:
            "Unauthorized", 401, {"Access-Control-Allow-Origin": "*"}
    #else return a a message and 401 status
    "Unauthorized", 401, {"Access-Control-Allow-Origin": "*"}

    '''
def run():
    app.run(port=8080, host='0.0.0.0')

if __name__=="__main__":
    run()
    