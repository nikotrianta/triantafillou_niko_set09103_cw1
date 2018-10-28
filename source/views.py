from . import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/dungeons')
def dungeons():
	return render_template('dungeons.html')

@app.route('/mythics')
def mythics():
	return render_template('mythics.html')

@app.route('/characters')
def characters():
	return render_template('characters.html')

@app.route('/uploads', methods=['POST', 'GET'])
def uploads():
	return render_template('uploads.html')
	if request.method == 'POST':
	 f = request.files['datafile']
	 f.save('static/images/')
	 return "File uploaded"
	else:
	 return render_template('uploads.html'), 200
