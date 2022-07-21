
class Student: 
    #constructor
    def __init__( self,  first_name, last_name, age, instructor, course ):
            #Attributes
            self.first_name = first_name
            self.last_name =   last_name
            self.age = age
            self.instructor = instructor
            self.course = course
        # Method
    def print_info( self ):
        print( f"name: {self.first_name}  {self.last_name}" )
        print( f"Age: {self.age}" )
        print( f"Instructor: {self.instructor}" )
        print( f"Course: {self.course}" )
            
        
class Course:
        def __init__( self, data ):
            self.name = data["name"]
            self.instructors = data["instructors"]
            self.program = data["program"]





def update instructor( sle, )
python = {
    "name" : "Python/Flask",
    "instructors" : [ "Alfredo Salazar", "Spencer Rauch", "Tylor Tybault" ],
    "program" : "Full Stack"
}
course_python = Course()
            
#Creating an object / Making an instance of the Student class
student_alex = Student( "Alex", "Miller", 20, "Nichole", "Web Fundementals")
print( student_alex )

print( student_alex.first_name, student_alex.last_name, student_alex.age )