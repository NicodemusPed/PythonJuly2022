from flask_mysql.Users_Crud.mysqlconnection import connectToMySQL

class Todo:
    def  __init__( self, data ):
        self.id = data[ 'data' ]
        self.id = data[ ' description' ]
        self.id = data[ 'status' ]
        self.id = data[ 'created_at' ]
        self.id = data[ 'updated_at' ]
        self.id = data[ 'user.id' ]

    @classmethod
    def get_all ( cls ):
        query = "SELECT * "
        query += "FROM todos;"
        
        result = connectToMySQL( ' todos_db' ).query_db( query )
        list_todos = [ ]
        for todo in result:
            list_todos.append( cls( todo ) )
        return list_todos

    @classmethod
    def create( cls, data ):
        query = "InNSERT INTO todos ( description, status, user_id )"
        query += "VALUES( %( description)s, %(status)s, %(user_id)s );"
        
        result= connectToMySQL( 'todos_db' ).query_db( query, data  )
        return result 
        

# """
# SELECT
# get_one()
# get_all()

# INSERT
# create() 
# save()

# UPDATE
# update_one()
# edit_one()

# DELETE
# delete_one()
# remove_one()
# """