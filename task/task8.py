# A student will not be allowed to sit in exam if his/her attendance is less than 75%.

# Take following input from user

# Number of classes held - 7856

# Number of classes attended. - 856 80%

# And print

# percentage of class attended

# Is student is allowed to sit in exam or not.



classHeld = int(input('Enter no of classes held         : '))
classAtte = int(input('Enter no of classes attended     : '))

if classAtte <= classHeld:
    percentage = (classAtte/classHeld)*100
    status = ""

    if percentage < 75:
        status = "student is not allowed to sit in exam"
    else:
        status = "student is allowed to sit in exam"

    print(percentage, status)

else:
    print("Invalid Info...")