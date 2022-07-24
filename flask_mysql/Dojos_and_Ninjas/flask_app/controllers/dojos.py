from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.controllers.ninjas import Ninja


@app.route('/')
def dojos():
    return redirect('/dojos')

@app.route('/dojos')
def dojo():
    return render_template("dojos.html",dojos=Dojo.get_all())

@app.route('/dojos/show')
def show():
    return render_template("dojos_show.html")

@app.route('/dojo/show',methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojos.html', dojo=Dojo.get_with_ninjas(data))


