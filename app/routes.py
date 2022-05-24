from flask import redirect, url_for
from flask import request
from flask import render_template
from app import app
from video.cloud import cloud
from app import db
database = db.Db()


@app.route('/')
@app.route('/index')
def index():
    return render_template('list.html', people=database.entries)

@app.route('/delname', methods=['POST', 'GET'])
def delname():
    if request.method == 'POST':
        id = int(request.form['id'])
        database.remove(id)
    return redirect(url_for('index'))

@app.route('/edname', methods=['POST', 'GET'])
def edname():
    if request.method == 'POST':
        id = int(request.form['id'])
        name = request.form['name']
        amount = request.form['amount']
        database.edit(id, name, amount)
    return redirect(url_for('index'))

@app.route('/addname', methods=['POST', 'GET'])
def addname():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        database.add(name, amount)
    return redirect(url_for('index'))

@app.route('/generate', methods=['POST', 'GET'])
def generate():
    names, amount = database.names()
    maxamount = database.maxamount
    cloud.generate_cloud(names, amount, maxamount)
    return redirect(url_for('index'))
