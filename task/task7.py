# Write a program to print absolute value of a number entered by user. E.g.-

# INPUT: 1        OUTPUT: 1

# INPUT: -1        OUTPUT: 1

n = int(input('Enter a number: '))

if n < 0:
    n *= -1

print("absolute value is :", n)