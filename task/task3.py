# Take two int values from user and print greatest among them.

a = int(input('Enter first no: '))
b = int(input('Enter second no: '))

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print('Both are equal')
