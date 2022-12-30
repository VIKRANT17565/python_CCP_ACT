# f = open('myFile.txt', 'w')
# print('name of file', f.name)
# print('file mode', f.mode)
# print('readable', f.readable())
# print('writable', f.writable())
# print('file has closed', f.closed)
# f.close()
# print('file has closed', f.closed)


# f =open('covid.txt', 'a')
# f.write('\n NGP is full vaccinated city')
# f.close()
# print('file operation done')


# f =open('covid.txt', 'w')
# myList = ['vikrant', 'singh']
# f.writelines(myList)      # her we can only pass list of strings not int and float
# f.close()
# print('file operation done')


# with open('myFile.txt', 'w') as f:
#     f.write('Anuj\n')
#     f.write('Ayush\n')
#     f.write('Vikrant\n')
#     print('file has closed', f.closed)

# print('file has closed', f.closed)


import csv
f = open('student.csv', 'a', newline='')
a = csv.writer(f)
# a.writerow(['studentId', 'rollNo', 'name', 'mobileNo'])
stuId = int(input('Student ID : '))
rollno = int(input('Student roll no. : '))
name = input('Student Name : ')
mobileno = int(input('Student mobile no.: '))

a.writerow([stuId, rollno, name, mobileno])
