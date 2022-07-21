from flask import Flask, render_template
app = Flask(__name__)
# our index route will handle rendering our form

@app.route('/')
def hello_world():
    return 'Hello World!'
    return render_template("index.html")

@app.route('/dojos')
def dojos():
    return 'All Dojos'
    return render_template("index.html")

@app.route('/dojos/show')
def show():
    return "list all dojos"

if __name__ == "__main__":
    app.run(debug=True)

