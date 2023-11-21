from flask import Flask, jsonify, request
import os
import json

app = Flask(__name__)


f = open('data.json')


data = json.load(f)


@app.route('/infilation')
def send_inflation():
  date = request.args.get('date')
  for i in data:
    print(i)
    if date==i['date']:
      return jsonify(i)


@app.route('/')
def hello_world():
  return "Hello World"
