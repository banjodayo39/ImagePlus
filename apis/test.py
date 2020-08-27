# Importing the required libraries
from flask import Flask, request, jsonify, abort, request,redirect, send_file
import numpy as np
import cv2
import argparse 
import os
import logging 
from PIL import Image
import uuid
from werkzeug.utils import secure_filename

UPLOAD_DIR = "../uploads"
ALLOWED_EXTENSIONS = [".png",".jpg",".jpeg",".jfif"]

app = Flask(__name__)
app.config["UPLOAD_DIR"] = UPLOAD_DIR

def is_file_valid(filename):
    """ This checks if a filename is valid """
    return filename.split(".")[-1].lower() in ALLOWED_EXTENSIONS

def cv2_decode(req):
    """ Decode image file data using OpenCV """
    arr = np.frombuffer(req.read(), np.uint8)
    return cv2.imdecode(arr , cv2.IMREAD_UNCHANGED)

def upload_file(file, filename):
    """ Function to upload files to local directory (To be replaced with AWS S3 Buckets) """
    if os.path.splitext(filename)[1] not in ALLOWED_EXTENSIONS:
        abort(400)
    file.save(os.path.join(app.config['UPLOAD_DIR'], filename ))
    data = {
        "message": "Successfully saved !"
    }
    return jsonify(data)

@app.route("/resize", methods = ["POST"])
def resize_img():
    """ Endpoint for resizing images """

    if request.method == "POST":
        scale = int(request.args["scale"])
    
        f, filename = request.files.get("file"), secure_filename(request.files.get("file").filename)
        upload_file(f, filename)
        img = cv2.imread(os.path.join(app.config["UPLOAD_DIR"], filename))
        (h,w) = img.shape[:2]
        new_w = int(w * (scale/100))
        new_h = int(h * (scale/100))
        resized_image = cv2.resize(img, (new_w, new_h))
        cv2.imwrite(os.path.join(app.config["UPLOAD_DIR"], filename), resized_image)

        data = {
                "message": "Images resized successfully by {}%".format(str(scale)), 
                "New image dimension": [new_w, new_h]
            }

        return send_file(os.path.join(app.config["UPLOAD_DIR"], filename), attachment_filename = filename, as_attachment= True)

@app.route("/filter", methods = ["POST"])
def filter():
    """ Basic endpoint for filtering """
    if request.method == "POST":

        mode = request.args["mode"]
        f, filename = request.files.get("file"), secure_filename(request.files.get("file").filename)
        upload_file(f, filename)
        img = cv2.imread(os.path.join(app.config["UPLOAD_DIR"], filename))

        if mode == "grayscale":
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imwrite(os.path.join(app.config["UPLOAD_DIR"], filename), img)

        return send_file(os.path.join(app.config["UPLOAD_DIR"], filename), attachment_filename = filename, as_attachment= True)
        



        
if __name__ == '__main__':
    app.run(debug = True)

