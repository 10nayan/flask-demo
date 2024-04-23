from flask import Flask, jsonify, request
from models import db, User
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://demo_user:Demo123@localhost:5432/demo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/api/get-all")
def get_all():
    try:
        all_users = [user.json_serializable() for user in User.query.all()]
        return jsonify({"users": all_users}), 200
    except:
        db.session.rollback()
        return jsonify({"status": False}), 400

@app.route("/api/create", methods=["POST"])
def create():
    name = request.json.get("name")
    gender = request.json.get("gender")
    dob = request.json.get("dob")
    try:
        user = User(name=name, gender=gender, dob=dob)
        db.session.add(user)
        db.session.commit()
        return jsonify({"user": user.json_serializable(), "status": True}), 200
    except:
        db.session.rollback()
        return jsonify({"status": False}), 400
        


        
        

if __name__ == "__main__":
    app.run(debug=True, port=5000)