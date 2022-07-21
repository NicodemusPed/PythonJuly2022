
class Animal:
    def __init__( self, name, owner ):
        self.name = name
        self.owner = owner
        
        def print_info( self ):
            print( f"Name of Animal: {self.name}" )
            print( f"Owner: {self.owner}" )
            
        def walk_animal( self ):
            raise NotImplementedError