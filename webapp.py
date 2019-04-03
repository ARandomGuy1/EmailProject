import os
from flask import Flask, redirect, url_for, session, request, jsonify
from flask import render_template
from flask_mail import Mail
import pprint


app = Flask(__name__)

@app.route("/")
def render_home():
	return render_template("home.html")
	
@app.route("/p1")
def render_page1():
	return render_template("page1.html")

app.debug = False

app.secret_key = os.environ['SECRET_KEY'] 


if __name__=="__main__":
    app.run(debug=False)