from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '4c14ff04a3c6d1ca1fff4b57'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from main.routes import routes