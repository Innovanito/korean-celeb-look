from flask import Flask, request, jsonify
import util
from flask_cors import CORS


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5500/UI/app.html"}})


@app.route('/classify_image', methods=['POST', 'GET'])
def classify_image():
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.header.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/hello')
def hello():
    return "Hello World!"


if __name__ == "__main__":
    print("Starting Python Flask Server For Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)
