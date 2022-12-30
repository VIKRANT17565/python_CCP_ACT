# def add():      # called function
#     print(2+2)

# add()   #calling function

########################## types of arguments in python

# 1. default
# 2. positional
# 3. keyWord
# 4. variable length



########################## example ##########################


########################## no arguments
def login():
    while True:
        username = input('enter username : ')
        passowrd = input('enter passowrd : ')
        if username == passowrd:
            print('login successfully')
            break
        else:
            print('you have entered wrong credentials')

# login()


########################## positional arguments
def info(firstname, lastname):
    print('First name =', firstname)
    print('Last name =', lastname)


# info('vikrant', 'singh')



def add(num1, num2):
    return num1+num2

# print(add(2, 3))

# result = add(10, 7)
# print(result)


def arithmatic(a, b):
    r = a+b
    n = a*b
    m = a-b
    return r, n, m  #in python returning multiple valuse at a time is possible

result = arithmatic(10, 5)
# print('results =', result)


########################## keyword arguments
def func(fname, lname):
    print('hi', fname)
    print('hi', lname)

# func(fname='vikrant', lname='singh')

# fname = input('Enter first name : ')
# lname = input('Enter last name : ')
# func(fname=fname, lname=lname)


########################## default arguments
def func2(city = 'Nagpur'):
    print('I am from', city)

# func2('delhi')
# func2('LA')
# func2()


########################## variable length arguments
def name(*name):
    print(name)

name('vikrant', 'singh', 'ayush', 101)


