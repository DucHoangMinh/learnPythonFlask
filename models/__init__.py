from flask_sqlalchemy import SQLAlchemy

from routes import app
db = SQLAlchemy(app)