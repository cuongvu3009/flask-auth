from models import User, db
from config import ApplicationConfig
from flask import Flask

app = Flask(__name__)
app.config.from_object(ApplicationConfig)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
