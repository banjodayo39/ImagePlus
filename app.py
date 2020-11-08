import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from PIL import Image
from werkzeug.utils import secure_filename
import numpy as np
import cv2
from features import basic

UPLOAD_FOLDER = 'static/images/'

app = Flask(__name__)
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/feature', defaults={'feature': 'resize'})

@app.route('/upload-image/<string:feature>', methods=['GET', 'POST'])
def upload(feature):
    if request.method == "POST":
        if request.files:
            file = request.files['image']
            if file.filename == '':
                flash('No image selected for uploading')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                print("secure filename dir: ", dir(filename))
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print('upload_image filename: ' + filename)
                flash('Image successfully uploaded and displayed')
                print("file name", filename)
                f = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                img = cv2.imread(f)
                if img is not None:
                    print(img)
                    if feature == 'resize':
                        edges = basic.pencil_sketch(img)
                        new_filename = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                        cv2.imwrite(new_filename, edges)
                    return render_template('./utilities/upload.html', filename=filename)
                else:
                    print("This guy is none")    
    return render_template('./utilities/upload.html')
'''
@app.route("/predict", methods=["POST"])
def predict():
    # Initialize result:
    result = {"success": False}
    if flask.request.method == "POST":
        if flask.request.files.get("image"):
            # Read input image in PIL format:
            image = flask.request.files["image"].read()
            image = Image.open(io.BytesIO(image))
            # Pre-process the image to be classified:
            image = preprocessing_image(image, target=(224, 224))
            # Classify the input image:
            with graph.as_default():
            predictions = model.predict(image)
            results = imagenet_utils.decode_predictions(predictions)
            result["predictions"] = []
            # Add the predictions to the result:
            for (imagenet_id, label, prob) in results[0]:
            r = {"label": label, "probability": float(prob)}
            result["predictions"].append(r)
            # At this point we can say that the request was dispatched successfully:
            result["success"] = True
            # Return result as a JSON response:
    return flask.jsonify(result)    
'''

@app.route('/upload-img')
def resizeimg():
    return render_template('./utilities/upload.html')


@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='images/' + filename), code=301)


if __name__ == "__main__":
    app.run(debug=True)
