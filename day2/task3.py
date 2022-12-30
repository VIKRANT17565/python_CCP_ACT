# Assignment 

# getPersonalInfo()
# getCollegeDetails()
# getMarksCalculate()
# showMarks()


width = 80
def getPersonalInfo():
    global name
    # print('='*width)
    name = input('                     Enter name: ')
    # print('='*width)

    pass

def getCollegeDetails():
    global clgName, yr, className, rollNo
    clgName = input('                    Enter college name: ')
    yr = input('                    Enter year: ')
    # className = input('                    Enter year: ')
    rollNo = input('                    Enter rollno: ')
    sem = input('                    Enter sem: ')

def getMarksCalculate():
    global maths, daa, cn, os, ssic, totalMarksObt, totalMarks, percent
    print("                    Enter marks")
    maths = int(input('                    Maths: '))
    daa = int(input('                    DAA: '))
    cn = int(input('                    CN: '))
    os = int(input('                    OS: '))
    ssic = int(input('                    Soft Skills: '))

    totalMarksObt = maths+daa+cn+os+ssic
    totalMarks = 500

    percent = (totalMarksObt/totalMarks)*100

def showMarks():
    print('='*width)
    print()
    print(' '*20 + 'College Name:', clgName)
    print()
    print('='*width)

    print('-'*width)
    print()
    print(' '*20 + 'Student Name:', name)
    print(' '*20 + 'Current year:', clgName)
    print(' '*20 + 'Current SEM :', clgName)
    print()
    print('-'*width)

    print('-'*width)
    print()
    print('|',' '*15 + 'Subjects ', 'Marks', '  Total Marks'+' '*40+'|')

    print('|',' '*15 + 'Maths:   ', maths,   '     100'+' '*40+'|')
    print('|',' '*15 + 'DAA:     ', daa,     '     100'+' '*40+'|')
    print('|',' '*15 + 'CN:      ', cn,      '     100'+' '*40+'|')
    print('|',' '*15 + 'OS:      ', os,      '     100'+' '*40+'|')
    print('|',' '*15 + 'SSIC:    ', ssic,    '     100'+' '*40+'|')
    print()
    print('-'*width)

    print('-'*width)
    print()
    print('|',' '*15 + 'Total marks obtained:   ', clgName, ''+' '*35+'|')
    print('|',' '*15 + 'DAA:     ', clgName, ''+' '*35+'|')
    print()
    print('-'*width)
    
    


getPersonalInfo()
getCollegeDetails()
getMarksCalculate()
showMarks()