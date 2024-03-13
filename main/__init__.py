from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '4c14ff04a3c6d1ca1fff4b57'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

db = SQLAlchemy(app)
from main.routes import routes