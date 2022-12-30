# p1 = int(input('enter paper1 mark : '))
# p2 = int(input('enter paper2 mark : '))
# p3 = int(input('enter paper3 mark : '))
# p4 = int(input('enter paper4 mark : '))
# p5 = int(input('enter paper5 mark : '))

# pract1 = int(input('enter pract1 mark : '))
# pract2 = int(input('enter pract2 mark : '))

# if p1 >= 40 and p2 >= 40 and p3 >= 40 and p4 >= 40 and p5 >= 40 and pract1 >= 40 and pract2 >= 40:
#     print('you are pass')
# else:
#     print('you anr fail')

# total = p1+p2+p3+p4+p5+pract1+pract2

# percent = total/7.0

# print('total =', total)
# print('percentage = ', percent)
###############################################################################################################

# ch = str(input('enter any character : '))

# if ch == 'a' or ch == 'A' or ch == 'e' or ch == 'E' or ch == 'i' or ch == 'I' or ch == 'o' or ch == 'O' or ch == 'u' or ch == 'U':
#     print('vowel')
# else:
#     print('not vowel')

###############################################################################################################

c = str(input('enter any character : '))
n = ord(c)

if n >= 97 and n <= 122:
    print('char is lower case')
elif n >= 65 and n <= 90:
    print('char is upper case')
elif n >= 48 and n <= 57:
    print('char is digit')
else:
    print('char is special char')
