import urllib.request
from flask import Flask, render_template, request, make_response, redirect
import numpy as np
import cv2
import os
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":

        if request.files:
            image = request.files["image"]
            print(image)

            return redirect(request.url)
        return render_template("index_html")


@app.route('/canny', methods=['GET'])
def canny_processing():
    url_link = 'https://imgs.xkcd.com/comics/python.png'
    with urllib.request.urlopen(request.get('url')) as url:
        image_array = np.asarray(bytearray(url.read()), dtype=np.uint8)

    img_opencv = cv2.imdecode(image_array, -1)

    gray = cv2.cvtColor(img_opencv, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 100, 200)

    retval, buffer = cv2.imencode('.png', edges)

    response = make_response(buffer.tobytes())
    response.headers['Content-Type'] = 'image/jpeg'

    return response


if __name__ == "__main__":
    app.run(port=455, debug=True)
