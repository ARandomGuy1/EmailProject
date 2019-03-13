from flask import Flask, redirect, url_for, session, request, jsonify
from flask import render_template
from flask_mail import Mail
import pprint
import os

app = Flask(__name__)

app.debug = False

app.secret_key = os.environ['SECRET_KEY'] 
