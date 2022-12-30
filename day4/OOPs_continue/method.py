## Type of mathod

####################################################### instance method

# class Student:
#     def __init__(self, name, rollno, mob):
#         self.name = name
#         self.rollno = rollno
#         self.mob = mob
    
#     def display(self):          # instance method
#         print(self.name, self.rollno, self.mob)
    

# Student = Student("Vikrant", 1001, 9656583298)

# Student.display()


####################################################### static method


class Student:
    @staticmethod       #decorator
    def get_personal_details(firstName, lastName):
        print("Your personal detail : ", firstName, lastName)
    
    @staticmethod
    def contact_details(mobo_no, rollno):
        print("Your contact detail : ", mobo_no, rollno)
    

Student.get_personal_details("Vikrant", "singh")
Student.contact_details(6598659874, 1001)