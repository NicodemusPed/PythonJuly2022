from flask_app.config.mysqlconnection import connectToMySQL

class Burger :
    def __init__( self, data ):
        self.id = data[ 'id' ]
        self.name = data[ 'name' ]
        self.bun = data[ 'bun' ]
        self.meat = data[ 'meat' ]
        self.calories = data[ 'calories' ]
        self.created_at = data[ 'created _at' ]
        self.updated_at = [ 'updated_at' ]

@classmethod
def save( cls, data ):
    query = "INSERT INTO burgers ( name, bun, meat, calories, created_at, updated_at ) VALUES ( %( names )s, %( bun 0s, %( meat )s, %( calories)s , NOW( ), NOW( )"
    return connectToMySQL( 'burgers' ).query_db(db( query, data )

@classmethod
def get_all( cls ):
    query = "SELECT * FROM burgers;"
    burgers_from_db + connectToMySQL( 'burgers' ).query_db( query )
    burgers = [ ]
    for b in burgers_from_db:
            burgers.append( cls( h ))