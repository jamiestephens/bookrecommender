# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 13:05:12 2021

@author: Administrator
"""

from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes