from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	session.pop('name', None)
	return 'Hello, World, are you still there??'

@app.route('/home', methods = ['POST', "GET"], defaults = {'name': 'Stranger'})
@app.route('/home/<name>')
def home(name):
	return render_template('home.html', name = name)
