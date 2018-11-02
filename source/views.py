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
	return render_template('dungeonslist/fh.html')

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

@app.route('/characters')
def characters():
	return render_template('characters.html')

@app.route('/war')
def war():
	return render_template('war.html')

@app.route('/pal')
def pal():
	return render_template('pal.html')

@app.route('/hun')
def hun():
	return render_template('hun.html')

@app.route('/rog')
def rog():
	return render_template('rog.html')

@app.route('/pri')
def pri():
	return render_template('pri.html')

@app.route('/sha')
def sha():
	return render_template('sha.html')

@app.route('/mag')
def mag():
	return render_template('mag.html')

@app.route('/wlk')
def wlk():
	return render_template('wlk.html')

@app.route('/mon')
def mon():
	return render_template('mon.html')

@app.route('/dru')
def dru():
	return render_template('dru.html')

@app.route('/dea')
def dea():
	return render_template('dea.html')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404