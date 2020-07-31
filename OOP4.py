# Demonstration of constructors

class Science:
    def __init__(self,name,standard,optional): #Constructor
        self.name = name
        self.standard = standard
        self.optional = optional

    def about(self): # Methods
        return(f"My name is {self.name} and I read in {self.standard} and my optional subject is {self.optional}")       

carry = Science("Carry Gupta", "X", ["Computer Science","Biology"])
# print(carry.name, carry.standard)
print(carry.about())