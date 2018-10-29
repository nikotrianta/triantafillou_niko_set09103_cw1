from . import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/home')
def home():
	return render_template('home.html')

@app.route('/experience')
def experience():
	return render_template('experience.html')

@app.route('/raiding')
def raiding():
	return render_template('raiding.html')

@app.route('/dungeons')
def dungeons():
	return render_template('dungeons.html')

@app.route('/dungeonslist')
def dungeonslist():
	return render_template('dungeonslist.html')

@app.route('/raid')
def raid():
	return render_template('raid.html')

@app.route('/mythics')
def mythics():
	return render_template('mythics.html')

@app.route('/characters')
def characters():
	return render_template('characters.html')
