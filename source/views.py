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
	return render_template('dungeonslist/kr.html')

@app.route('/ml')
def ml():
	return render_template('dungeonslist/ml.html')

@app.route('/sob')
def sob():
	return render_template('dungeonslist/sob.html')

@app.route('/sots')
def sots():
	return render_template('dungeonslist/sots.html')

@app.route('/td')
def td():
	return render_template('dungeonslist/td.html')

@app.route('/tos')
def tos():
	return render_template('dungeonslist/tos.html')

@app.route('/ur')
def ur():
	return render_template('dungeonslist/ur.html')

@app.route('/wm')
def wm():
	return render_template('dungeonslist/wm.html')

@app.route('/raid')
def raid():
	return render_template('raid.html')

@app.route('/factions')
def factions():
	return render_template('factions.html')

@app.route('/classes')
def characters():
	return render_template('classes.html')

@app.route('/war')
def war():
	return render_template('classlist/war.html')

@app.route('/pal')
def pal():
	return render_template('classlist/pal.html')

@app.route('/hun')
def hun():
	return render_template('classlist/hun.html')

@app.route('/rog')
def rog():
	return render_template('classlist/rog.html')

@app.route('/pri')
def pri():
	return render_template('classlist/pri.html')

@app.route('/sha')
def sha():
	return render_template('classlist/sha.html')

@app.route('/mag')
def mag():
	return render_template('classlist/mag.html')

@app.route('/wlk')
def wlk():
	return render_template('classlist/wlk.html')

@app.route('/mon')
def mon():
	return render_template('classlist/mon.html')

@app.route('/dru')
def dru():
	return render_template('classlist/dru.html')

@app.route('/dea')
def dea():
	return render_template('classlist/dea.html')

@app.errorhandler(404)
def page_not_found(error):
	return render_template('page_not_found.html'), 404