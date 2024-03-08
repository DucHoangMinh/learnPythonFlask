from flask import Flask, render_template

app = Flask(__name__)
app.app_context().push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'

from routes import routes
