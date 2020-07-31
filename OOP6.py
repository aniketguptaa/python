class Employee:

    def __init__(self,name,standard,subject):
        self.name = name
        self.standard = standard
        self.subject = subject

    def about(self):
        return(f"The name is {self.name} and class is {self.standard} and subject is {self.subject}")
        
    @classmethod
    def split_it(cls, string): #using class methods as alternative constructors
        list_name = string.split(",")
        # print(type(list_name)) this is a list
        return cls(list_name[0],list_name[1],list_name[2])
        # return cls(*string.split(",")) # Alternative way

carry = Employee.split_it("carry,X,Mathematics")
print(carry.about())




