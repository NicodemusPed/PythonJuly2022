class Student:
    # Constructor
    def __init__( self, first_name, last_name, age, instructor, course ):
        # Attributes
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.instructor = instructor
        self.course = course
    # Method
    def print_info( self, message ):
        print( message )
        print( f"Name: {self.first_name} {self.last_name}" )
        print( f"Age: {self.age}" )
        print( f"Instructor: {self.instructor}" )
        print( f"Course: {self.course}" )

# Creating an object / Making an instance of the Student class
student_alex = Student( "Alex", "Miller", 20, "Nichole", "Web Fundamentals" )
student_martha = Student( "Martha", "Smith", 25, "Alfredo", "Python" )

list_students = []
list_students.append( student_alex )
list_students.append( student_martha )

for student in list_students:
    student.print_info( "Hey there!" )#Instructor code