from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)


f = open('data.json')


data = json.load(f)

f2 = open('data2.json')


data2 = json.load(f2)

f3 = open('data3.json')


data3 = json.load(f3)

@app.route('/infilation')
def send_inflation():
  date = request.args.get('date')
  for i in data["montly_inflations_2023"]:
    if date==i["date"]:
      return jsonify(i)


@app.route('/foreigntrade')
def foreign_trade():
  date = request.args.get('date')
  for i in data2["foregintrade"]:
    if date==i["date"]:
      return jsonify(i)
    
@app.route('/gross-national-product')
def gross_national_product():
  date = request.args.get('date')
  for i in data3["gross-national-product"]:
    if date==i["date"]:
      return jsonify(i)

@app.route('/')
def hello_world():
  return "Hello World"
