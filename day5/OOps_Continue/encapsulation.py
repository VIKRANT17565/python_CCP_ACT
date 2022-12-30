# ## Private variable '__x'

# class Base():
#     def __init__(self):
#         print("Parent class constructor called")
#         self.a = "YCCE"     #public variable
#         self.__c = "IIM"    #private vaiable

# class Derived(Base):
#     def __init__(self):
#         # Calling constructor of Base class
#         Base.__init__(self)

#         print("Calling private member of Base class")
#         # print(self.__c)


# # Driver code
# obj1 = Derived()

# # print(obj1.a)
# # print(obj1.c)

# obj2 = Base()

# # print(obj2.c)

################################################################################

# ## Protected variable '_x'

class Base():
    def __init__(self):
        print("Parent class constructor called")
        self._a = 2     #protected variable

class Derived(Base):
    def __init__(self):
        # Calling constructor of Base class
        Base.__init__(self)

        print("Calling private member of Base class")
        print(self._a)


# Driver code
obj1 = Derived()
