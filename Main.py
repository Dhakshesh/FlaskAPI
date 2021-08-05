from flask import Flask,jsonify,request
from Data import data
app=Flask (__name__)
@app.route('/')
def home():
	return jsonify({
		'data':data,'message':'success'
	})
if __name__=='__main__':
	app.run()