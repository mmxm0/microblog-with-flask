'''
Created on May 30, 2018

@author: marta.maria.x.melo
'''
from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
