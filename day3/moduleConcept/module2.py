# # first way to import any module using file name

# import module1

# module1.square(2)
# module1.login('singh', 'singh')
# print(module1.pi)

#############################################################################

# # second way to import any module using file name as alias

# import module1 as mod

# mod.square(2)
# mod.login('singh', 'singh')
# print(mod.pi)
# # print(module1.pi) #error

#############################################################################

# # third way to import any module using from keyword
# # only import specified variables, functions and classes

# from module1 import pi, square, login

# square(2)
# login('singh', 'singh')
# print(pi)
# # print(module1.pi) #error

#############################################################################

# # forth way to import any module using *

# from module1 import*

# square(2)
# login('singh', 'singh')
# print(pi)
# # print(module1.pi) #error