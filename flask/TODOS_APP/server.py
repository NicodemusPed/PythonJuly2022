from flask import Flask,  render_template, request, redirect, session
app = Flask(__name__)

app.secret_key =  "My Secret Codes"

@app.route('/')
def hello_world():
    return 'Hello World its July 2022!'

@app.route( '/python' )
def display_python_messsage():
    return "Hello, this is a different route?python."

@app.route( '/hello/<first_name>/<last_name>' )
def greet_person( first_name, last_name ):
    print( f"Hey there { first_name, last_name }" )
    return f"Howdy, { first_name} { last_name }"

@app.route( '/info/<name>/<age>' )
def display_info( name, age ):
    print( type( name ), type( age) )
    print( age + 5 )
    return  "Name: {name} Age: {age}"

list_of_users = [ {
    "first_name" : "Alex",
    "last_name" : "Miller" ,
    "id" : 1
},
{
    "first_name" : "Martha",
    "last_name" : "Smith" ,
    "id" : 2
},
{
    "first_name" : "Roger",
    "last_name" : "Anderson" ,
    "id" : 3
} ]

list_of_todos = [ {
    "description" : "Learn Python",
    "status" : "complete",
    "id" : 1,
    "user_id" : 1
},
{
    "description" : "Learn OOP",
    "status" : "complete",
    "id" : 2,
    "user_id" : 1
},
{
    "description" : "Learn routes in Flask",
    "status" : "in_progress",
    "id" : 3,
    "user_id" : 2
},
{
    "description" : "Learn POST",
    "status" : "in_progress",
    "id" : 4,
    "user_id" : 3
} ]

@app.route( '/todos' )
def get_todos():
    if "logged_user" not in session:
        return redirect('user/login' )
    logged_uid = int(session[ 'logged_user' ] )  - 1
    user = list_of_users[ 'logged_uid' ]
    return render_template( 'todos.html' , todos = list_of_todos , user=user )    

@app.route( '/todo/form')
def display_todo_form():
    return render_template( 'todo_form.html', users = list_of_users )

@app.route( '/todo/new' ,  methods = [ 'POST' ] )
def create_todo():
    new_todo = {
        "id" : int( request.form[ 'id' ]),
        "descripton" : request.form[ 'staus' ],
        "status" : request.form[ 'status'] ,
        "user_id" : int (request.form[ 'user_id' ] )
    }
    list_of_todos.append( new_todo )
    return redirect( '/todos' )

@app.route( '/ user/process_login', methods= [ 'POST' ] )
def process_login():
    session[ 'logged_user' ] = request.form[ ' user_id' ]
    return redirect( '/todos/ ')

@app.route( '/user/logout' )
def user_logout():
    session.pop( 'logged_user' )
    return redirect( '/user/login' )

@app.route( '/user/login' )
def user_login():
    return render_template( "user_login.html" , users = list_of_users )

    if __name__=="__main__":        
        app.run(debug=True) 