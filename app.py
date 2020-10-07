import os
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
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

@app.route('/upload-image', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        if request.files:
            file = request.files['file']
            if file.filename == '':
                flash('No image selected for uploading')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                print('upload_image filename: ' + filename)
                flash('Image successfully uploaded and displayed')
                return render_template('./utilities/upload.html', filename=filename)
    return render_template('./utilities/upload.html')
    
@app.route('/upload-img')
def resizeimg():
    return render_template('./utilities/upload.html')


@app.route('/display/<filename>')
def display_image(filename):
	#print('display_image filename: ' + filename)
	return redirect(url_for('static', filename='images/' + filename), code=301)


if __name__ == "__main__":
    app.run(debug=True)
