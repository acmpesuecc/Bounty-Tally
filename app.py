import pymongo
from bson.json_util import dumps
import json
from flask import Flask, request, render_template, session, redirect, url_for, flash, Response, abort, render_template_string, send_from_directory
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
application = app
CORS(app)

USERNAME = os.environ.get("DB_USERNAME")
PASSWORD = os.environ.get("DB_PASSWORD")

#Loads the Database and Collections
mongo = pymongo.MongoClient("mongodb+srv://"+USERNAME+":"+PASSWORD+"@cluster0.uy3bn.mongodb.net/Hacktoberfest2020?retryWrites=true&w=majority", maxPoolSize=50, connect=True)
db = pymongo.database.Database(mongo, 'Hacktoberfest2020')


@app.route('/')
def hello():
	return "Hi, this is the API server"


@app.route('/tests/build_test')
def build_test():
	return "Passed"

@app.route('/scores')
def get_scores():
	BountyData = pymongo.collection.Collection(db, 'BountyData')
	data = json.loads(dumps(BountyData.find()))
	res = {}
	for i in data:
		if i['contributor'] in res:
			res[i['contributor']] += i['points']
		else:
			res[i['contributor']] = i['points']
	return res
