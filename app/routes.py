from app import app
from bottle import template
from bottle import static_file

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./app/static')

@app.get('/')
@app.get('/index')
def index():
    return template('game_board') 

@app.post('/')
@app.post('/index')
def index():
	return request.json;
