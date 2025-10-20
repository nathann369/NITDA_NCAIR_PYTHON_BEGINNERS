# Object Oriented Programming

# class Objects:

#     def __init__(self, name, age):
#         self.name = name #this is an attribute of the class
#         self.age = age
#         # print(name)
    
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age
#     def set_age(self, age):
#         return self.age

    # def meaw(self):
    #     print("meawwww")
    # def bark(self):
    #     return "whoooo whoo"
    # def add_one(self, x):
    #     return x + 1

# O = Objects("Nate", 19)
# O.set_age(27)
# print(O.get_name())
# print(O.get_age())
# o = Objects("george")
# o = Objects() #this is a new instance of the class cat and that class will be represented by C. Instantition

# -----------------------------------------------
# o.meaw()
# print(o.bark())
# print(o.add_one(7))
# print(type(o))

# ---------------------------------------------------------------------------------------------------------------------

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
    
class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.student = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

s1 = Student("Nate", 20, 90)
s2 = Student("Steve", 19, 80)
s3 = Student("Tk", 18, 69)

course = Course("Python", 2)
course.add_student(s1)
course.add_student(s2)
# print(course.student[0].name)