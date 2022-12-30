# Write a Python program to find the median of three values.

# Expected Output:

# Input first number: 15

# Input second number: 26

# Input third number: 29

# The median is 26.0

l = list(map(int, input().split()))

l.sort()


print("The median of three values :", l[1])