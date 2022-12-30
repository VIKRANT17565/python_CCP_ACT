## Type of inheritance in python
"""
single
multilevel
multiple

############################ syntax

############################ single inherit

class derived_class(bsae_Class):
    '''
    code block
    '''


"""


############################ single inherit


# class College:
#     def college_name(self):
#         print ("Modern College")

# class Student(College):
#     def student_info(self):
#         print('Name   : Vikrant singh')
#         print('Branch : Computer engineering')

# obj = Student()

# obj.college_name()
# obj.student_info()


############################ multilevel inherit


# class College:
#     def college_name(self):
#         print ("Modern College")

# class Student(College):
#     def student_info(self):
#         print('Name   : Vikrant singh')
#         print('Branch : Computer engineering')

# class Exam(Student):
#     def subject(self):
#         print("Subject1: DE")
#         print("Subject2: MATh")
#         print("Subject3: c-language")

# obj = Exam()

# obj.college_name()
# obj.student_info()
# obj.subject()


############################ multiple inherit

class SubjectMarks:
    maths = int(input("Enter marks of maths : "))
    DE = int(input("Enter marks of DE : "))
    c = int(input("Enter marks of C language : "))
    english = int(input("Enter marks of english : "))

class PracticalMarks:
    cPract = int(input("Enter practical marks of C language : "))


class Result(SubjectMarks, PracticalMarks):
    print("if student pass in both subject and practical paper then pass")

    def total(self):
        if self.maths >= 40 and self.DE >= 40 and self.c >= 40 and self.english >= 40 and self.cPract >= 40:
            print("Pass")
        else:
            print("Fail")

obj = Result()
obj.total()