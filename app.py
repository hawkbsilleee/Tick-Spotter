from flask import Flask, render_template, url_for, request, redirect, session, flash, send_from_directory
from datetime import timedelta
from werkzeug.utils import secure_filename
import os 
from predict import predictor 

app = Flask(__name__)

# Folder path for image uploads
UPLOAD_FOLDER = '/Users/ethan.seiz24/Desktop/TICKSPOTTERWEBSITE/uploads'
ALLOWED_EXTENSIONS = {'jpg', 'jpeg'}
# randomly generated encryption key 
SECRET_KEY = os.urandom(24).hex()

app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    """
    Check if the filetype is allowed
    returns: True if filename's .suffix is in ALLOWED_EXTENSIONS 
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# routes to home page 
@app.route('/')
def index():
    return render_template('index.html')

# routes to about page 
@app.route('/about')
def about():
    return render_template('about.html')

# downloads uploaded file to local upload folder 
@app.route('/uploads/<name>')
def download_file(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

# receives post request from form 
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # if there is a post request from the form 
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        # If the user selects a file and the file has an allowed extension 
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            results = predictor(file)
            # generate results page with predictions 
            return render_template('results.html', prediction = results[0], certainty = results[1], 
            img_file="uploads/"+filename) 
    # otherwise render the upload template form 
    return render_template('upload.html')

if __name__ == "__main__":
    app.run(debug=True)