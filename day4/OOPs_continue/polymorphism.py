'''
how to archive polymorphism

1. compile time polymorphism
    overloading
2. runtime polymorphism (dynamic or late binding)
    overriding


'''


#################################### polymorphism

# ##E Example 1

# class Principal:
#     def role(self):
#         print("I am managing all activity of college")
# class Dean:
#     def role(self):
#         print("Deam : I am decision taking person")
# class Hod:
#     def role(self):
#         print("Hod : I have responsibility of teachers and Students")
# class Faculty:
#     # error
#     def responsibility(self):
#         print("Faculty : I have to complete syllabus successfully")

# def func(obj):
#     obj.role()

# campus = [Principal(), Dean(), Hod(), Faculty()]

# for obj in campus:
#     func(obj)


# ### Example 2

# # error dega ye code
# class Deposit:
#     def __init__(self, cash):
#         self.cash = cash
    
# d1 = Deposit(1000)
# d2 = Deposit(2000)

# print(d1 + d2)

# solution
### operator overloading

# class Deposit:
#     def __init__(self, cash):
#         self.cash = cash

#     def __add__(self, other):           # magic method
#         return self.cash + other.cash
    
# d1 = Deposit(1000)
# d2 = Deposit(2000)

# print(d1+d2)


# ### method overloading
# ## python don't support method overloading

# class Arithmatic:
#     def add(self, a):
#         print(a)
#     def add(self, a, b):
#         print(a+b)
#     def add(self, a, b, c):
#         print(a+b+c)

# obj = Arithmatic()
# obj.add(2)
# obj.add(2, 5)
# obj.add(2, 3, 4)


# ### constructor overloading
# ## python don't support constructor overloading

# class Arithmatic:
#     def __init__(self):
#         print("first")
#     def __init__(self, a):
#         print("second")
#     def __init__(self, a, b):
#         print("third")

# obj = Arithmatic()
# obj = Arithmatic(2)
# obj = Arithmatic(1, 2)


# ### method overriding

# class Father:
#     def bike(self):
#         print("Harley Devidson")
    
#     def laptop(self):
#         print("laptop with 2GB Ram and 500 GB HDD i3 processor")

# class Aman(Father):
#     def laptop(self):
#         print("As per my programming software requarment this is not cool for me")
#         print("laptop with 8 GB Ram and 1TB HDD i7")

#         super().laptop()

# obj = Aman()
# obj.bike()
# obj.laptop()

# ### constructor overriding


class Father:
    def __init__(self):
        print("constructor of parent")


class Child(Father):
    def __init__(self):
        print("Constructor of child")
        # super().__init__()

obj = Child()