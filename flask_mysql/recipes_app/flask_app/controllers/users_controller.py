from flask_app import app
from flask import render_template, request, redirect, flash
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
        user_exists = User.get_one_to_validate_email( request.form )
        if user_exists == False:
            flash( " this email already exists!", "error_registration_email" )
            return redirect( '/' )
        data = {
            **request.form,
            "password" : bcrypt.generate_password_hash( request.form[ 'password' ] )
        }

        User.create( data )
        return redirect ( '/' )
    # time 135in Youtube

