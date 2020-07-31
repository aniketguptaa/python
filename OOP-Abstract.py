# abstract method in python

from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def printarea(self): #mandatory method
        return()

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.lenght = 43
        self.breadth = 6
    def printarea(self):
        return self.lenght * self.breadth

class Triangle(Rectangle,Shape):
    type = "Square"
    side = 3
    
    # def __init__(self):
    #     self.base = 4
    #     self.height = 6

rect1 = Rectangle()
print(rect1.printarea())
# triangle1 = Triangle()
# print(triangle1.printarea())

