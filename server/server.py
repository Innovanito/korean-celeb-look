from flask import Flask, request, jsonify
import util

app = Flask(__name__)


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
