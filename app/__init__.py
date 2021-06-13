# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 13:05:12 2021

@author: Administrator
"""

from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models