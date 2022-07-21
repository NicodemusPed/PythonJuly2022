from flask import Flask, render_template, session, redirect

app = Flask(__name__)    

app.secret_key="careers"

@app.route( '/' )
def index():
    if 'count' not in session:
        session[ 'count' ] = 0
    session[ 'count' ] +=1
    return render_template("index.html", count=session[ 'count' ])

@app.route( '/plus2' )
def plus2():
    session[ 'count' ] +=1
    return redirect( '/' )

@app.route( '/reset' )
def reset():
    session[ 'count' ]
    return redirect( '/' )

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

