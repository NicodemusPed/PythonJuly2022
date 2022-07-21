from flask import Flask, render_template, request, redirect, flash

app = Flask (__name__ )

app.secret_key = "triplethreat"

@app.route( '/' )
def index():
    return render_template( "survey.html" )

@app.route( "/result", methods= [ 'POST' ]  )
def result():
    if len( request.form[ "name" ])<1:
        flash( " Cannot be Blank" )
        return redirect( "/" )
    
    if len( request.form [ "comments" ])<1:
        flash( " Cannot be Blank" )
        return redirect( "/" )
    
    if len( request.form[ "comments" ])>120:
        flash( "Max of 120 characters" )
        return redirect ( '/' )

    else:
        name = request.form[ "name" ]
        dojo_location = request.form [ "dojo_location"]
        favlanguage = request.form [ "favlanguage" ]
        comments = request.form [ "comments" ]
        return render_template( "result.html", name = name, dojo_location = dojo_location, favlanguage = favlanguage, comments = comments )
    
@app.route( "/admin" )
def admin():
    print( "user is not 'admin', redirected to '/' ")
    return redirect( '/' )

if __name__ == "__name__":
    
        app.run( debug=True )