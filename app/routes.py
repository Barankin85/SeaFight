from app import app
from bottle import template, request, static_file
from models import game

@app.route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./app/static')

@app.get('/')
@app.get('/index')
def index():
    return template('game_board', game = game) 

@app.post('/')
@app.post('/index')
def index():
    game.fire(request.json['x'], request.json['y'])
    
    if game.winner:
        isYouWinner = game.winner == game.you

        game.start()

        if isYouWinner:
            return "You are winner!"
        else:
            return "Your enemy won!"

@app.post('/reset')
def reset():
    game.start()

