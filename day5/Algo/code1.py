n = int(input("Enter amount : "))

# n = 1355
# 1000 = 1
# 100  = 3
# 50   = 1
# 5    = 1

note1000 = n // 1000
n = n% 1000

note100 = n // 100
n = n% 100

note50 = n // 50
n = n% 50

note5 = n // 5
n = n% 5

print("1000 :", note1000)
print("100  :", note100)
print("50   :", note50)
print("5    :", note5)
