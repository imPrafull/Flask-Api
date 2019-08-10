from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
import firebase_admin
from firebase_admin import credentials
import os

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
this_folder = os.path.abspath(os.path.dirname(__file__))
cert_file = os.path.join(this_folder, 'where-smytutor-firebase-adminsdk-yyd3u-af8e7dc9b2.json')
cred = credentials.Certificate(cert_file)
default_app = firebase_admin.initialize_app(cred)

from app import routes, models