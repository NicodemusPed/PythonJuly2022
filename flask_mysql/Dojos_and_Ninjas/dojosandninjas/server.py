from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return redirect('/dojos')

@app.route('/dojos')
def dojos():
    print ('Nicodemus')
    return render_template("dojos.html")



if __name__ == "__main__":
    
    app.run(debug=True)

