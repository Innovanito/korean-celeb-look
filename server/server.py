from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/classify_image', methods=['POST', 'GET'])
def classify_image():
  return "Hello World"

if __name__ == "__main__":
  app.run(port=5000)