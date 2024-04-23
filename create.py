from app import app
from models import db

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://demo_user:Demo123@localhost:5432/demo"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()

