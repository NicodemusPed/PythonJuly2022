from classes.animal import Animal

class Cat( Animal ):
    def __init__( self, name, owner, breed, age ):
        super().__init__( name, owner , breed )
        self.age = age
        
                          