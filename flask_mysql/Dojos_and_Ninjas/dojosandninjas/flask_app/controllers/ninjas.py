from flask import render_template, render_template, redirect

from flask_app import app
from flask_app.models.ninja import ninjas


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")




