from flask_app import app
from flask import render_template, request, redirect, flash, session
from flask_app.models.recipe_model import Recipe


@app.route( '/recipies' )
def display_recipes():
    if 'email' not in session:
        return redirect( '/' )
    Recipe.get_all_with_users()
    return render_template( 'recipes.html' )

@app.route( '/recipe/new' )
def display_create_recipe():
    if 'email' not in session:
        return redirect( '/' )
    return render_template( "create_recipe.html" )

@app.route( '/recipe/create', methods = [ 'POST' ] )
def create_recipe():
    if Recipe.validate_recipe( request.form ) == False:
        return redirect( '/recipe/new' )

    data = {
        **request.form,
        "user_id" : session[ 'user_id' ]
    }
    Recipe.create( data )

