from datetime import time
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://bob:admin@localhost/email"
app.debug = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app.controller import controller
from app.model import email