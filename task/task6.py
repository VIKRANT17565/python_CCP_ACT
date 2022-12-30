# Take input of age of 3 people by user and determine oldest and youngest among them.

a = int(input("Enter age of first person :"))
b = int(input("Enter age of second person :"))
c = int(input("Enter age of third person :"))

maxAge = 0
minAge = 0

if a >= b and a >= c:
    maxAge = a
    if b < c:
        minAge = b
    else:
        minAge = c


if b >= a and b >= c:
    maxAge = b
    if a < c:
        minAge = a
    else:
        minAge = c

if c >= a and c >= b:
    maxAge = c
    if a < b:
        minAge = a
    else:
        minAge = b

print("max age:", maxAge, "min age:", minAge)