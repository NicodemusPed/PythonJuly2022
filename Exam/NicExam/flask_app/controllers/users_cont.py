from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.user_model import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt( app )

@app.route( '/' )
def display_login():
    return render_template( 'login.html' )

@app.route( '/user/registration', methods = [ 'POST' ] )
def process_registration():

    if User.validate_registration( request.form ) == False:
        return redirect( '/' )

    user_exists = User.get_one( request.form )
    if user_exists != False:
        flash( "Email exists, Try again", "error_registration_email" )
        return redirect( '/' )

    data={
        **request.form,
        "password" : bcrypt.generate_password_hash( request.form [ 'password' ] )
    }

    user_id = User.create( data )

    session[ 'first_name' ] = data[ 'first_name' ]
    session[ 'email' ] = data[ 'email' ]
    session[ 'user_id' ] = user_id

    return redirect( '/dashboard' )

@app.route( '/user/login', methods = [ 'POST' ] )
def process_login():
    current_user = User.get_one( request.form )

    if current_user != None:
        if not bcrypt.check_password_hash( current_user.password, request.form[ 'password' ] ):
            flash ( "Invalid Credentials", 'error_registration_password' )
            return redirect( '/' )

        session[ 'first_name' ] = current_user.first_name
        session[ 'email' ] = current_user.email
        session[ 'user_id' ] = current_user.id

        return redirect( '/dashboard' )
    else:
        flash ( "Invalid Credentials", 'error_registration_password')
        return redirect( '/' )

@app.route( '/dashboard' )
def display_dashboard():
    if 'email' not in session:
        return redirect( '/' )
    return render_template( 'dashboard.html' )

