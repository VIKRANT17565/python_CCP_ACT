# yn = 'yes'

# while yn == 'yes':
#     print('1. add')
#     print('2. mul')
#     print('3. div')
#     print('4. sub')
#     ch = int(input('\nEnte your choice : '))
#     n1 = int(input('Ente first no: '))
#     n2 = int(input('Ente second no: '))

#     if ch == 1:
#         print('result =',n1+n2)
#     elif ch == 2:
#         print('result =',n1*n2)
#     elif ch == 3:
#         print('result =',n1/n2)
#     elif ch == 4:
#         print('result =',n1-n2)
#     else:
#         print('invalid choice!')

#     yn = input('Do you want to continue(yes/no):')


l = [2, 3, 4, 4, 2, 5, 2, 1, 5, 5, 4, 4]

_map = {}

for i in l:
    _map[i] = 0

for i in l:
    _map[i] += 1

for i in _map.keys():
    pair = int(_map[i]/2)
    if pair == 0:
        continue
    print(i, '=', pair)