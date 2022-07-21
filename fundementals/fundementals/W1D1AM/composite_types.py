
# js - array [items, items, items] : Python - lists
grades = [9.8, 8.7, 7.6]

print(grades)
print(len(grades))
#add element to a list JS-.push(element) : Python.append()

grades.append(10.0)
print(grades)

grades_copy=grades #reference to the previous array

grades_copy[0]=4.5
print(grades_copy)
print(grades)

# objects in JS are Dictionaries in Python
student={
    "fist_name" : "Nic",
    "last_name": "Pederson",
    "age" : 50,
    "grade":9.8,
    "stack" : "python/Flask",
    "passed" : True
}
    
print(student, ["first_name"])
l_n="last_name"
print(student[l_n])
    
student["instructor"]="Alfredo Salazr"
    
print(student);
    
    #tuple
course=("python", "4 weeks", "Spencer Rauch")
print(course)
course[0]="Web Fundementals"
print(course[0]);
    