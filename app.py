from flask import Flask, request
import config

app = Flask(__name__)
@app.route('/', methods=['GET'])
def index():
    return "Hello World!"