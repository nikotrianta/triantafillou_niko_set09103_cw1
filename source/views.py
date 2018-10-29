from . import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/experience')
def experience():
	return render_template('experience.html')

@app.route('/raiding')
def raiding():
	return render_template('raiding.html')

@app.route('/dungeons')
def dungeons():
	return render_template('dungeons.html')

@app.route('/mythics')
def mythics():
	return render_template('mythics.html')

@app.route('/characters')
def characters():
	return render_template('characters.html')
