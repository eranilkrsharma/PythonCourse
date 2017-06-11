# functions in class is called methods but its same
students = []
"""
self is instance of class itself, like this in Java  and self should be first parameter in methods  

Static methods can be called with instance 
"""
class Student:

    def add_student(self, name , student_id =122):
        student = {"name": name , "student_id":student_id}
        students.append(student)


student = Student()
student.add_student("Anil")

print students

"""

Constructor methods -- it's hidden until overridden 

"""

class Student1:

    def __init__(self, name , student_id =122):
        student = {"name": name , "student_id":student_id}
        students.append(student)
#   overridding methods provided by class
    def __str__(self):
        return "Student"


student = Student1("Sharma")

print students

print student
