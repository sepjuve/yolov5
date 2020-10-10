import os
from app import app 
import urllib.request
from flask import Flask, flash, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'mp4'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

@app.route('/', methods=['POST'])
def upload_image():
	if 'file' not in request.files:
		flash('No file part')
		return redirect(request.url)
	file = request.files['file']
	if file.filename == '':
		flash('No image selected for uploading')
		return redirect(request.url)
	if file and allowed_file(file.filename):
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		#print('upload_image filename: ' + filename)
		flash('Image successfully uploaded and displayed')
		os.system('python /content/yolov5/detect.py --weights /content/drive/My\ Drive/Project/2020/best.pt --img 416 --conf 0.4 --source static/uploads/'+filename)
		ext = filename.split(".")
		return render_template('upload.html', filename=filename, ext=ext[1])
	else:
		flash('Allowed image types are -> png, jpg, jpeg, gif')
		return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename): 
	#print('display_image filename: ' + filename)
  return send_from_directory('inference/output/', filename)
	#return redirect(url_for('static', filename='inference/output/' + filename), code=301)

@app.route('/download/<filename>')
def download(filename):
  return send_from_directory('inference/output/', filename+'.avi')



if __name__ == "__main__":
    app.run()