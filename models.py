from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(10,))
    dob = db.Column(db.Date)
    adult = db.Column(db.Boolean())
    last_login = db.Column(db.DateTime())

    def json_serializable(self):
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'dob': self.dob.isoformat() if self.dob else None,
            'adult': self.adult,
            'last_login': self.last_login.isoformat() if self.last_login else None
        }