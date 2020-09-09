from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/features')
def features():
    return render_template('features.html')

@app.route('/resize-img')
def resizeimg():
    return render_template('./utilities/resizeimage.html')

if __name__ == "__main__":
    app.run(debug=True)
