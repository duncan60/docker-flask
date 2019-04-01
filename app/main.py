from flask import Flask
import json
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/test')
def test():
    return json.dumps({
        "message": "Validation Failed",
        "result": {
          "name": "test"
        }
    })