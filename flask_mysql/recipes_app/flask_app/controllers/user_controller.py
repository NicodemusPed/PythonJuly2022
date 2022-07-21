from flask_app import app
from flask import render_template

@app.route( '/' )
def display_login():
    return render_template( 'login.html" ')

@app.route( '/user/registration', methods = [ 'POST' ] )
def process_registration():
