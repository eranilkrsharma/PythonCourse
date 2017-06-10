"""
This file contains flow examples from course

"""

num = 5

if num == 5:
    print "Input is 5"

else:
    print "Number is NOT 5"

###########################################

# Truthy and falsy values in python

if num:
    print "Input has truthy value , 0 is falsy value"

str = "this is string"

if str:
    print "string has truthy value as length is greater than 0"

str = ""

if str:
    print "string has falsy value as length is greater than 0"

if not str:
    print "condition has truthy value as NOT is added"

# and , or is used for multiple conditions

#Ternary If Statement

a = 1
b = 2

print "bigger" if a > b else "smaller"

#list

student_name = [] # Empty list

student_name = ["Mark","James","Jas"]

# access values
print "This first value in list is :" +student_name[0]
print "This last value in list is :" +student_name[-1]

# add new value in list

student_name.append("anil")

print  student_name

# check if value exist in List

print "anil" in student_name

# len(student_list) = 4 #How many elements in the list

# delete element from list

del student_name[2]

print student_name

# LIST SLICING

print student_name[1:]
print student_name[1:-1]


# Loops

for name in student_name:
    print "Student name is {0}".format(name)


""" Range is used for incremental loops"""
#While loops

x = 0
while x < 10:
    print x
    x += 1

#### Dictionaries are like json with key value pairs

student = {

    "name" :"Mark",
    "Student_id": 123,
    "feedback": None

}

print student
print student["name"]

try:
    print student["last_name"]
except KeyError:
    print "Key error in code"
print student.keys()
print student.values()





