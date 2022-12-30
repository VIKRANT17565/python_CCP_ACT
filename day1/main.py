####################### data type #######################
# p1 = 50
# p2 = 60.55

# name = 'vikrant'

# pass1 = True

# print(type(p1))
# print(type(p2))
# print(type(name))
# print(type(pass1))

####################### string #######################

# name = 'vikrant'
# print(name[0:10:3])
# print(name[2:])
# print(name[:5])
# print(name[2:6])
# print(name[:])
# print(name[6])

####################### memory management #######################

# maths = 50
# chem = 50
# phy = 50

# eng = 40
# hindi = 45

# print("maths",id(maths))
# print("chem",id(chem))
# print("phy",id(phy))
# print("eng",id(eng))
# print("hindi",id(hindi))

# math2 = 55
# print("old maths value",id(55))
# math2 = 65
# print("new maths value",id(65))
# # previous value of 'maths' will be cleared by the "GARBEG COLLECTOR"

####################### input from user #######################

# n = input('enter a number : ')      # always accept as string

# print(type(n))

####################### type casting #######################

# n = int(input('enter a number : '))      # always accept as string

# print(type(n))

####################### type casting #######################

# print(int(3.14))
# print(int(True))
# print(int(False))
# print(int('3'))
# # print(int(3.14 + 10j))
# # print(int('3.14'))
# # print(int('vikrant'))

####################### type casting to float #######################

# print(float(3.14))
# print(float(True))
# print(float(False))
# print(float('3.14'))
# print(float('3'))
# # print(float(3.14 + 10j))
# # print(float('vikrant'))


####################### type casting to float #######################

# print(complex(3.14))
# print(complex(3.14 + 10j))
# print(complex(True))
# print(complex(False))
# print(complex('3.14'))
# print(complex('3'))
# print(complex(True, False))
# print(complex(3, 4))
# # print(complex('vikrant'))


####################### type casting to float #######################

# print(bool(3.14))
# print(bool(3.14 + 10j))
# print(bool(True))
# print(bool(False))
# print(bool('3.14'))
# print(bool('3'))
# print(bool(''))
# print(bool(0))
# print(bool('vikrant'))


####################### list #######################

# myList = ['vikrant', 'ashish', 'rahul', 'ankit',
#           'anuj', 'ayush', 67, True, 1+3j, 99.99]
# print(myList)

# print(myList[0])
# print(myList[2])
# print(myList[4])
# print(myList[-2])
# print(myList[4: 7])
# print(myList[:])
# print(myList[2:])
# print(myList[:6])

# myList.append("latest element")
# print(myList)
# myList.append("new latest element")
# print(myList)


# list functions

# myList.insert()
# myList.remove()
# myList.copy()

# l = [2, 5, 3, 6, 4, 7, 1]

# l.sort(reverse= True)

# print(l)

# list vs tuple
# -> if the requirement is fixed then use tuple
#     and if it is not fixed use list

####################### tuple #######################

# myTuple = ("vikrant", "singh", "ayush", "anuj", "vimal", 67, True, 1+3j, 99.99)
# print(myTuple)
# print(type(myTuple))
# # myTuple[2] = "akash"
# print(myTuple)

####################### set #######################

mySet = {1, 2, 'vikrant', 5.66, 'anuj', 'ayush', 33}

# set functions
# mySet.add(90)
# mySet.discard(3)          used when not sure the value is present or not
# mySet.remove(3)           used when the value is present
# print(mySet)

# newSet = {9, 'singh', 'vikrant', "anuj"}

# nayaSet = newSet.union(mySet)
# print(nayaSet)

# print(mySet.intersection(newSet))

# print(mySet.difference(newSet))
# print(newSet.difference(mySet))

####################### frozenset #######################

# fs = frozenset(mySet)
# print(type(fs))
# print(fs)

####################### dict #######################

# myDic = {101: 'vikrant', 102: 'anuj', '102': 'ayush', 103: "akash"}

# print(myDic)
# print(myDic[102])
# myDic[103] = 'tushar'
# print(myDic)
# myDic[104] = 'new value'
# print(myDic)


