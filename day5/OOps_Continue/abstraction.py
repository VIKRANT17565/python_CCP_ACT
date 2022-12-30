## Abstraction

# Python not support abstract class
# It uses Abstract base class (abc) to use abstration

from abc import ABC , abstractmethod

## Example 1

# from abc import ABC , abstractmethod

# class Programming(ABC):

#     @abstractmethod
#     def training(self):
#         pass

#     @abstractmethod
#     def placement(self):
#         pass

# class Ashish(Programming):
#     def training(self):
#         print("C, C++, Java")
    
#     def placement(self):
#         print("Java placement")


# class Ankush(Programming):
#     def training(self):
#         print("python | django")
    
#     def placement(self):
#         print("Python placement")

# class Prashant(Programming):
#     def training(self):
#         print("machine learning")
    
#     def placement(self):
#         print("Data science placement")


# obj1 = Ashish()
# obj1.training
# obj1.placement()

# obj2 = Ankush()
# obj2.training
# obj2.placement()

# obj3 = Prashant()
# obj3.training()
# obj3.placement()

## Example 2


# from abc import ABC , abstractmethod

class Irctc(ABC):

    @abstractmethod
    def bookTicket(self):
        pass

    @abstractmethod
    def display_details(self):
        pass


class MakeMyTrip(Irctc):
    def bookTicket(self):
        print("         welcome to Make My Trip      ")
        self.source = input("Enter source : ")
        self.destination = input("Enter destination : ")
        self.date = input("Enter date :")

    def display_details(self):
        print("sourace      : ", self.source)
        print("destination  : ", self.destination)
        print("date         : ", self.date)

class GoIbibo(Irctc):
    def bookTicket(self):
        print("         welcome to BOIBIBO      ")
        self.source = input("Enter source : ")
        self.destination = input("Enter destination : ")
        self.date = input("Enter date :")

    def display_details(self):
        print("sourace      : ", self.source)
        print("destination  : ", self.destination)
        print("date         : ", self.date)

class Yatra(Irctc):
    def bookTicket(self):
        print("         welcome to Yatra.com      ")
        self.source = input("Enter source : ")
        self.destination = input("Enter destination : ")
        self.date = input("Enter date :")

    def display_details(self):
        print("sourace      : ", self.source)
        print("destination  : ", self.destination)
        print("date         : ", self.date)

obj1 = MakeMyTrip()
obj1.bookTicket()
obj1.display_details()

obj2 = GoIbibo()
obj2.bookTicket()
obj2.display_details()

obj3 = Yatra()
obj3.bookTicket()
obj3.display_details()