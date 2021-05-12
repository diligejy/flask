from flask import Flask, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    count = 0
    count += 1
    return jsonify(text='Hello, World', count=count)
