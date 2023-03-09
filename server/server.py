from flask import Flask, request, jsonify
import util


app = Flask(__name__)


@app.route('/classify_image', methods=['POST', 'GET'])
def classify_image():
    # 이미지의 b64 string 데이터를 잘 가져오는지 print 찍어보기
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    print('response type in server 2', type(response))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/give_string', methods=['POST'])
def give_string():
    string_data = request.form['string_data']

    response = jsonify(string_data)

    response.header.add('Access-Control-Allow-Origin', '*')

    print('response in give_string', response)

    return


if __name__ == "__main__":
    print("Starting Python Flask Server For Image Classification")
    util.load_saved_artifacts()
    app.run(port=5000)
