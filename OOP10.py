# Diamond Shape Problem
class A:
    def printit(self):
        print('I am in Class A')

class B(A):
     def printit(self):
        print('I am in Class B')

class C(A):
     def printit(self):
        print('I am in Class C')

class D(C,B):
    pass
    # class D(B,C)
    #  def printit(self):
    #     print('I am in Class D')

a = A()
b = B()
c = C()
d = D()

d.printit()