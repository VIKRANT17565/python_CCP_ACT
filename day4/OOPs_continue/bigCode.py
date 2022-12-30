choice = 0 # global variable
class Exam(object):
    def __init__(self):
        self.sname = None
        self.collegename = 0
        self.classname = 0
        self.rollno = 0
        self.login()

    def login(self):
        print("========================================================")

        username = input("Enter username: ")
        password = input("Enter password: ")

        print("========================================================")
        print()

        #Login Session
        if username == password:
            print("Login successfully")
            self.getdata()
        else:
            print("Login fail try again")

        print()

        # Enter Your Profile Details
    def getdata(self):
        self.sname =        input("Enter your Name : ")
        self.classname =    input("Enter your Class Name : ")
        self.collegename =  input("Enter your College Name : ")
        self.rollno =       input("Enter your Roll Number : ")
        print()

    #================================== End of Profile ==================================

        #static subject declartion
        print(" choose any branch for giving exam")
        print("1. Mechanical Engineering")
        print("2. Infomation Technology")
        print("3. Computer Science")
        print("4. Civil Engineering")
        print()

        choice = int(input("Enter your choice : "))

        if choice == 1:
            self.mechanical()
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        else:
            print("you have entered wrong choice")

    # called function
    def mechanical(self):
        print("1. First Semester")
        print("2. Second Semester")

        print("Enter your Semester Number")

        # logic part

        choice = int(input("Enter your choice : "))
        if choice == 1:
            #first_subj()
            print("Math")
        elif choice == 2:
            pass # second_subj()
    
    def information(self):
        print("1. First Semester")
        print("2. Second Semester")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            pass
        elif choice == 2:
            pass

    def computer(self):
        print("1. First Semester")
        print("2. Second Semester")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            pass
        elif choice == 2:
            pass

    def civil(self):
        print("1. First Semester")
        print("2. Second Semester")

        choice = int(input("Enter your choice : "))
        if choice == 1:
            pass
        elif choice == 2:
            pass


# object creation of class

# obj = Exam()
# obj.login()


# Claculation part

class Calculation(object):
    def __init__(self):
        self.stat = 0
        self.dmgt = 0
        self.cg = 0
        self.toc = 0
        self.math = 0
        self.total = 0
        self.percentage = 0
        self.ps = 0
        print()
        print("Do You Want To Put Examination ")
        print()
        Yes = input("Enter yes/no : ")
        if Yes == "yes":
            self.calculatemarks()
        else:
            print("Thank You For Visiting Here")
        print()
    
    def calculatemarks(self):
        self.stat = int(input("Enter Marks of Statistics        : "))
        self.dmgt = int(input("Enter Marks of DMGT              : "))
        self.cg =   int(input("Enter Marks of CG                : "))
        self.toc =  int(input("Enter Marks of TOC               : "))
        self.math = int(input("Enter Marks of Maths1            : "))
        print()

        if self.stat >= 40 and self.dmgt >= 40 and self.cg >= 40 and self.toc >= 40 and self.math >= 40:
            self.ps = "Pass"
            print("You are pass")
        else:
            self.ps = "Fail"
            print("You are fail")

        self.total = self.stat + self.dmgt + self.cg + self.toc + self.math
        self.percentage = self.total/5.0

# obj1 = Calculation()

#Assesment class

class Assesment(Exam, Calculation):
    def __init__(self):
        Exam.__init__(self)
        Calculation.__init__(self)

    def result(self):
        print("=========================================================================================================")
        print("                                                                                                         ")
        print("                                \tCollege Name:", self.collegename, "                                      ")
        print("                                                                                                         ")
        print("=========================================================================================================")
        
        print("|        Student Name: ", self.sname,        "\t                                                                |")
        print("|        Class Name  : ", self.classname,    "\t\t                                                                |")
        print("|        Roll NO     : ", self.rollno,        "\t\t                                                                |")
        print("=========================================================================================================")
        print("                                                                                                         ")
        print("  Subject Name   :   Total Marks :   Obtained Marks  :   ")

        print("                                                                                                         ")
        
        print(" Statictic     \t :", " 100"  "  \t :", self.stat,  "\t\t:")
        print(" DMGT          \t :", " 100"  "  \t :", self.dmgt,  "\t\t:")
        print(" CG            \t :", " 100"  "  \t :", self.cg,    "\t\t:")
        print(" TOC           \t :", " 100"  "  \t :", self.toc,   "\t\t:")
        print(" Math          \t :", " 100"  "  \t :", self.math,  "\t\t:")

        print("=========================================================================================================")
        print("                                                                                                         ")
        print("Result Status        :", self.ps, " ")
        print("Total Marks          :", "500", " ")
        print("Obtained Marks       :", self.total, " ")
        print("Percentage           :", self.percentage, " ")
        print("=========================================================================================================")


obj2 = Assesment()
obj2.result()