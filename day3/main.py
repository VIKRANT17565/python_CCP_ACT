# a = int(input('enter first no : '))
# b = int(input('enter second no: '))

# # print(a/b)
# try:
#     print(a/b)
# except:
#     print("Can't divide by Zero")

#############################################################

try:
    print(2/0)
except ZeroDivisionError as message:
    print("The description of exception:", message)


#############################################################


# try:
#     a = int(input('enter first no : '))
#     b = int(input('enter second no: '))
#     print(a/b)
# except ZeroDivisionError as message:
#     print("plz ensure that you can't divide any no by Zero: ", message)
# except ValueError as message:
#     print("Enter only integer no : ", message)


#############################################################


# try:
#     a = int(input('enter first no : '))
#     b = int(input('enter second no: '))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message)


#############################################################


# try:
#     a = int(input('enter first no : '))
#     b = int(input('enter second no: '))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message)
# except:
#     print('default except block')


############### error
# try:
#     a = int(input('enter first no : '))
#     b = int(input('enter second no: '))
#     print(a/b)
# except:
#     print('default except block')
# except (ValueError, ZeroDivisionError) as message:
#     print(message)


#############################################################


# try:
#     a = int(input('enter first no : '))
#     b = int(input('enter second no: '))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message)

# else:
#     print('else block: Everything is ok')


#############################################################


# try:
#     a = int(input('enter first no : '))
#     b = int(input('enter second no: '))
#     print(a/b)
# except (ValueError, ZeroDivisionError) as message:
#     print(message)

# finally:
#     print('finally block')


#############################################################


# try:
#     a = int(input('enter first no : '))
#     b = int(input('enter second no: '))
#     try:
#         print(a/b)
#     except ZeroDivisionError as message:
#         print(message)
# except ValueError as message:
#     print(message)


#############################################################

balance = 2000
if balance > 1000:
    raise Exception('your account balance is below a accessing limit')
else:
    print('amount has withdrawl')