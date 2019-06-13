from flask import Flask, request, jsonify
from flask_cors import CORS

import sys
import io
from imageio import imread
import base64
import cv2
import os
from captcha_to_text import get_text_from_captcha

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello from Flask'


@app.route('/', methods=['POST'])
def receive_b64_text():
    # base64 image
    b64_img = request.get_json()['base64']
    print(b64_img, file=sys.stderr)

    img = imread(io.BytesIO(base64.b64decode(b64_img)))

    cv2_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    cv2.imwrite("reconstructed.png", cv2_img)

    text = get_text_from_captcha('./reconstructed.png')
    print(text, file=sys.stderr)

    os.remove('./reconstructed.png')

    return jsonify({"captcha_text": text})

if __name__ == '__main__':
    app.run()