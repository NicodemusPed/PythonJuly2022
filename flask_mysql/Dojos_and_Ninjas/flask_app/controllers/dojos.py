from flask import render_template, redirect
from flask_app import app
from flask_app.models.dojo import dojo


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    return render_template("dojos.html",dojos=Dojo.get_all())

@app.route('/dojos/list')
def list():
    return render_template("dojos.html")

