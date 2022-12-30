# class New:
#     x = 10
#     def display(self):
#         print("hello python")

# obj = New()

# obj.display()
# print(obj.x)
# # print(obj.a)

##############################################################################

# class NewClass:
#     def __init__(self):
#         print("my name is constructor and I always execute first")


#     def show(self):
#         print("Welcom to class level programming")

# obj = NewClass()
# obj.show()

# obj2 = NewClass()


##############################################################################

# class Hod:
#     def __init__(self):
#         self.name = 'Sonali'
#         self.age = 21
#         self.empid = 1001
    
#     def info(self):
#         print('My name is :', self.name)
#         print('My Age is :', self.age)
#         print('My emp id is :', self.empid)

# obj = Hod()
# obj.info()


##############################################################################


# how many type of variable we can declayer inside class
# instance variable
# static variable
# local variable



# # instance variable inside constructor
# class Student:
#     def __init__(self):
#         self.f_name = 'Vikrant'
#         self.l_name = 'singh'
#         self.rollNo = 1001
#         self.branch = 'CS'
    
# obj =  Student()
# print(obj.__dict__)

# # instance variable inside instance method
# class Student:
#     def __init__(self):
#         self.s_name = 'Vikrant'
#         self.s_rollNo = 1001
#         self.s_branch = 'CS'
    
#     def getData(self):
#         self.s_mb = 4878787888788
    
# obj =  Student()
# # obj.getData()
# print(obj.__dict__)


# # instance variable outside class
# class Student:
#     def __init__(self):
#         self.s_name = 'Vikrant'
#         self.s_rollNo = 1001
#         # self.s_branch = 'CS'
    
#     def getData(self):
#         self.s_mb = 4878787888788
    
# obj =  Student()
# obj.getData()
# obj.s_branch = "CS"
# print(obj.__dict__)



# # deleting instance variable from class
# class Student:
#     def __init__(self):
#         self.s_name = input("Enter your name: ")
#         self.s_rollNo = 1001
#         # self.s_branch = 'CS'
    
#     def getData(self):
#         self.s_mb = 4878787888788
    
# obj =  Student()
# obj.getData()
# obj.s_branch = "CS"
# del obj.s_rollNo
# print(obj.s_name)
# print(obj.__dict__)



###################################################################################
## Day 4 ##


################################# Static variable #################################

# class New:
#     a = 10

#     def __init__(self):
#         self.name = "Vikrant"

# obj1 = New()
# obj2 = New()
# obj3 = New()
# # single memory is created for static variable i.e. a = 10


################################# example #################################

class College:
    collegeName = "Morden College"          #static variable (1 memory)

    def __init__(self):
        self.studentName = "Prashant"       #instance variable (3 memory)

    
principal = College()
student = College()
accountant = College()

print("principal=", principal.collegeName, '...', principal.studentName)
print("student=", student.collegeName, '...', student.studentName)
print("accountant=", accountant.collegeName, '...', accountant.studentName)

College.collegeName = "HBD"
principal.studentName = "Prashant jha"

print("principal=", principal.collegeName, '|', principal.studentName)
print("student=", student.collegeName, '|', student.studentName)
print("accountant=", accountant.collegeName, '|', accountant.studentName)
