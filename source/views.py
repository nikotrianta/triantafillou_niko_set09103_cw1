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

@app.route('/fh')
def fh():
	return render_template('fh.html')

@app.route('/kr')
def kr():
	return render_template('kr.html')

@app.route('/ml')
def ml():
	return render_template('ml.html')

@app.route('/sob')
def sob():
	return render_template('sob.html')

@app.route('/sots')
def sots():
	return render_template('sots.html')

@app.route('/td')
def td():
	return render_template('td.html')

@app.route('/tos')
def tos():
	return render_template('tos.html')

@app.route('/ur')
def ur():
	return render_template('ur.html')

@app.route('/wm')
def wm():
	return render_template('wm.html')

@app.route('/raid')
def raid():
	return render_template('raid.html')

@app.route('/mythics')
def mythics():
	return render_template('mythics.html')

@app.route('/characters')
def characters():
	return render_template('characters.html')
