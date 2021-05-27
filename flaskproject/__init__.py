"""
The flask application package.
"""
import os

import csrf as csrf
from flask import Flask

# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate


app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'flasknotely.db')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

import flaskproject.views
