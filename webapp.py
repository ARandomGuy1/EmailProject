import os
from flask import Flask, redirect, url_for, session, request, jsonify
from flask import render_template
from flask_mail import Mail, Message
import pprint

app = Flask(__name__)


app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'bengrawlings@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ["PASSWORD"]
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


@app.route("/")
def render_home():
	return render_template("home.html")
	
@app.route("/p1")
def render_page1():
	return render_template("page1.html")

@app.route("/p2")
def render_page2():
	session["date"] = request.args["date"]
	session["wins"] = request.args["wins"]
	session["games"] = request.args["games"]
	return render_template("page2.html")
	
@app.route("/p3")
def render_page3():
	#csv = "Month, 1958, 1959, 1960 \n "
	#msg = Message.attach("games.csv", "text/csv", csv)
	csv = "\"dateTime\",\"winsLosses\",\"gameNumber\",\"whatGame\",\"like\",\"gamesPerWeek\" \n \"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\""%(session["date"], session["wins"], session["games"], request.args["what"], request.args["like"], request.args["week"])
	msg = Message("CS project", sender = "bengrawlings@gmail.com", recipients = ["bengrawlings@gmail.com"])
	msg.body = ""
	msg.attach("games.csv", "text/csv", csv)
	mail.send(msg)
	#what = request.args['what']
	#like = request.args['like']
	#week = request.args['week']
	return render_template("page3.html")

	
#app.debug = True

app.secret_key = os.environ['SECRET_KEY'] 


if __name__=="__main__":
    app.run(debug=True)