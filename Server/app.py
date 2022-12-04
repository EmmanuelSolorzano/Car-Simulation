from flask import Flask, request, jsonify
import json
import agentpy as ap
from itertools import product
#Visualization
import seaborn as sns
import IPython 
import matplotlib.pyplot as plt 
import random

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "hi"

@app.route("/save_json", methods = ["GET", "POST"])
def save_json_file():
    data = request.json
    print(data)
    with open("json_file.json", "w+") as f:
        data = json.dumps(data, indent=4)
        f.write(data)
        print(f)
    return "JSON Saved"


@app.route("/get_json", methods=["GET", "POST"])
def get_json_file():
    data = request.json
    print(data)
    with open("json_file.json", "r+") as f:
        data = f.readlines()
    data = "\n".join(data)
    data = json.loads(data)
    return jsonify(data)

if __name__ == 'main':
    app.run(host='0.0.0.0', debug=True)


