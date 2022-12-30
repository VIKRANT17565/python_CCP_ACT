import csv


def createCSV():
    f = open('report.csv', 'a', newline='')
    a = csv.writer(f)
    a.writerow(['studentId', 'name', 'rollNo', 'emailId', 'address', 'mobileNo', 'p1', 'p2', 'p3', 'p4', 'p5', 'total', 'percentage', 'result'])
    f.close()


def studentDataInpt():
    f = open('report.csv', 'a', newline='')
    a = csv.writer(f)
    try:
        recordCount =   int(input('Enter no of record       : '))
    except ValueError as msg:
        print("\nInput error:", msg)
        studentDataInpt()
        
    i = 0
    while(i < recordCount):
        print('\n\nRecord of student', i+1)
        try:
            stuId =         int(input('Student ID               : '))
            name =              input('Student Name             : ')
            rollno =        int(input('Student roll no.         : '))
            emailId =           input('Student Email Id         : ')
            address =           input('Student Address          : ')
            mobileno =      int(input('Student mobile no.       : '))
            
            
            p1 =            float(input('paper1 MArks             :'))
            p2 =            float(input('paper2 MArks             :'))
            p3 =            float(input('paper3 MArks             :'))
            p4 =            float(input('paper4 MArks             :'))
            p5 =            float(input('paper5 MArks             :'))
        
            total = p1+p2+p3+p4+p5

            percentage = total/5

            if p1 > 40 and p2 > 40 and p3 > 40 and p4 > 40 and p5 > 40:
                result = 'pass'
            else:
                result = 'fail'
            a.writerow([stuId, name, rollno, emailId, address, mobileno, p1, p2, p3, p4, p5, total, percentage, result])
            print('\n\n\n')
            i += 1

        except(ValueError) as msg:
            print("\nInput error:", msg)
            print('\n*************** Enter data again! ***************\n')
    f.close()
            





def readStudentData():
    try:
        f = open('report.csv', 'r', newline='')
    except:
        print("\nfile not found...\n")
        return
    
    rd = csv.reader(f)

    idInput = int(input('\n\nEnter student Id : '))
    for i in rd:
        if i[0] == str(idInput):
            print(i,"\n\n")
            return
    print('----------------- Record not found -----------------\n\n')

    f.close()


while True:
    print('0. Exit')
    print('1. Enter student data')
    print('2. Read student record')

    try:
        ch = int(input('\nEnter your choice : '))
    except:
        
        continue

    if ch == 0:
        break
    elif ch == 1:
        try:
            f = open('report.csv', 'r', newline='')
        except:
            print('file not found')
            print('....................')
            print('New csv file created')
            createCSV()
        studentDataInpt()


    elif ch == 2:
        readStudentData()
    else:
        print('Invalid choice!')