students =[]

def add_student(name, student_id =12):
    student = {"name":name ,"student_id":student_id}
    students.append(student)
    print students

add_student("Mark") # If we have default value of parameter defined then we can skip that parameter
add_student("Anil", 23) # If parameter passed then default value will be overridden


# Simply pass any number of args
def var_args(name, *args):
    print name
    print args

var_args("Mark" , "This is args example" , 1, None)


# kwargs is used to pass key value pair in parameter list


def var_args(name, **kwargs):
    print name
    print kwargs["description"] , kwargs["id"]

var_args("Mark" , description = "This is args example" , id =1, feedback =None)

# this is to get input from console

name = raw_input("Enter the student name : ")
student_id = raw_input("Enter the student_id: ")

add_student(name, student_id)

# nested function is allowed in Python

# yield is used for generator

# Lambda function example


def double(x):
    return x * 2

# Convert this to lambda function which multiply the x with 2

doublel = lambda x: x * 2

print doublel(5)
print double(5)
