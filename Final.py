# importing required libraries
from flask import Flask
from flask_restful import Resource, Api
from flask import request
from dateutil import parser
import json 
import requests
from flask import send_file

# fetching data from source
requestJSON = requests.get("https://assignment-machstatz.herokuapp.com/excel")
rq=requestJSON.text
data=json.loads(rq)

app = Flask(__name__, static_url_path='')

# app = Flask(__name__)

@app.route("/")
def first():
	return "OK"


@app.route("/excelreport")
def excelreport():
    return app.send_static_file('excelreport.xlsx')

#creating REST API
@app.route("/total")
def query():
	args = request.args
	d=args["day"]
	Json={} # final data wil be stored in this
	totalWeight=0
	totalLength=0
	totalQuantity=0
	
	for i in data:
		dt = parser.parse(i["DateTime"]) 
		n=dt.strftime('%d-%m-%Y')
		if n==d:
			totalWeight+=i["Weight"]
			totalLength+=i["Length"]
			totalQuantity+=i["Quantity"]

	Json["totalWeight"]=totalWeight
	Json["totalLength"]=totalLength
	Json["totalQuantity"]=totalQuantity
	return Json;




if __name__ == "__main__":
	app.run(debug=True)



