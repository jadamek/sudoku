#================================================================
# - Sock Monkey Suduko Main Page Router				-
#----------------------------------------------------------------
#================================================================
from bottle import default_app, route
from src.Model.Board import Gameboard

@route('/')
def home_page():
    return 'Welcome to Sock Monkey Sudoku!'

@route('/test-board')
def board():
    return Gameboard.sayHello()

application = default_app()
