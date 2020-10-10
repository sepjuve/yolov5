from flask_ngrok import run_with_ngrok
from flask import Flask

UPLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__)
run_with_ngrok(app)   #starts ngrok when the app is run
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024