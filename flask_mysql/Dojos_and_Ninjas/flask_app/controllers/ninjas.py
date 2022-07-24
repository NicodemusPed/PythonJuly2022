from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html",ninjas=Ninja.get_all())

@app.route('/dojos/newninja')
def list():
    return render_template("ninjas.html")

@app.route('/ninjas/show',methods=['POST'])
def create():
    print(ninjas.form)
    Ninja.save(ninjas.form)
    return redirect('/dojos')


