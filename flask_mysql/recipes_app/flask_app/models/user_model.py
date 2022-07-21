from flask_app.config.mysqlconnection import connectTOMySQL

class User:
    def __init__( self, data ):
        self.id = data[ 'id' ]
        self.first_name = data[ 'first_name' ]
        self.last_name = data[ 'last_name' ]
        self.email = data[ 'email' ]
        self.password = data[ 'password' ]
        self.created_at = data[ 'created_at' ]
        self.updated_at = data[ 'updated_at' ]
        
    @staticmethod
    def validate_registration( data ):
        is_valid = True
        if len( data[ 'first_name' ] ) >2:
            flash( "Your first name needs to have at least 2 characters", "erro_registration_first_name" )

        