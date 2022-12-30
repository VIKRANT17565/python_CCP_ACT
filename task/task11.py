# Write a Python program to check a triangle is . 

# Note :

# An equilateral triangle is a triangle in which all three sides are equal.

# A scalene triangle is a triangle that has three unequal sides.

# An isosceles triangle is a triangle with (at least) two equal sides.


sd1 = float(input("Enter length of side 1: "))
sd2 = float(input("Enter length of side 2: "))
sd3 = float(input("Enter length of side 3: "))

if sd1 == sd2 and sd2 == sd3:
    print("Triangle is equilateral")
elif sd1 == sd2 or sd2 == sd3 or sd1 == sd3:
    print("Triangle is scalene")
elif sd1 != sd2 and sd2 != sd3:
    print("Triangle is isosceles")