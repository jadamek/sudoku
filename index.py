#================================================================
# - Sock Monkey Suduko Main Page Router				-
#----------------------------------------------------------------
#================================================================
from bottle import default_app, route
@route('/')
def home_page():
    return 'Welcome to Sock Monkey Sudoku!'
application = default_app()
