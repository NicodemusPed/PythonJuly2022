from re import template
from flask import Flask, render_template, request, redirect, session  # Import Flask --class to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key="THIS IS MY SECRET"

list_of_users=[ {
    "first_name" : "Alex",
    "last_name" : "Miller",
    "id" : 1
},
{
    "first_name" : "Martha",
    "last_name" : "Smith",
    "id" : 2
},
{
    "first_name" : "Roger",
    "last_name" : "Anderson",
    "id" : 3
},
{
    "first_name" : "Steve",
    "last_name" : "Getty" ,
    "id" : 4
} ]

list_of_todos=[ {
    "description" : "learn Python",
    "status" : "complete",
    "id" : 1,
    "user id" : 1
},
{
    "description" : "learn OOP",
    "status" : "complete",
    "id"  : 2,
    "user id" : 1
},
{
    "description" : "learn routes in Flask",
    "status" : "in_progress",
    "id"  : 3,
    "user id" : 2
},
{
    "description" : "learn POST",
    "status" : "in_progress",
    "id"  : 4,
    "user id" : 3
} ]

@app.route('/todos')
def get_todos():
    if "logged_user" not in session:
        return redirect('/user/login')
    logged_uid =int( session['logged_user'])
    user=list_of_users[logged_uid-1]
    
    return render_template( 'todos.html', todos = list_of_todos )

@app.route('/todo/form')
def display_todo_form():
        return render_template('todo_form.html', users=list_of_users)

@app.route( '/todo/new', methods=['POST'] )
def create_todo():
    new_todo={
        "id": int(request.form['id']),
        "description" : request.form['status'],
        "user_id" : int(request.form['user_id'])
    }   
list_of_todos.append(new_todo)
    return redirect('/todos')

@app.route('/user/process_login', methods=['POST'])
def process_login():
    session['logged_user']=request.form['user_id']
    
@app.route('/user/login')
def user_login():
    return render_template("user_login.html", users=list_of_users, user=user)

    return render_template('todos.html',todos)
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module --file    

@app.route('user/logout')
def user_logout():
    session.pop('logged_user')
    return redirect('/user/login')

    app.run(debug=True)