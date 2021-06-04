# -*- coding: utf-8 -*-
"""
Created on Fri Jun  4 13:28:09 2021

@author: Administrator
"""


import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'