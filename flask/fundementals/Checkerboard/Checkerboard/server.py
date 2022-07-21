from flask import Flask,  render_template 
app = Flask(__name__)

@app.route('/')
def checker_board():
    return render_template("index.html", a=8, b=8, color1='black', color2='green')

@app.route('/4')
def checker_board4():
    return render_template("index.html", a=4, b=4, color1='black', color2='green')

@app.route('/<int:x>/<int:y>')
def xy(x,y):
    print( x,y )
    return render_template("index.html", a=x, b=y, color='black', color2='chartruse')

if __name__=="__main__": 
    app.run(debug=True)