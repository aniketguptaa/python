# Single Level Inheritence
class Employee:
    def __init__(self,name,work):
        self.name = name
        self.work = work
    def about(self):
        print(f"The name is {self.name} and work is {self.work}")

    @staticmethod
    def print_from_Employee(string):
        print("It is a valuable Student of Employee")
        return()

class Student(Employee): #Single level inheritence

    @staticmethod
    def print_from_Student(string):
        print("It is a valuable Student of Student")
        return()

# carry = Student("Carry","Analyst")
# carry.about() #Printing from Employee
# carry.print_from_Employee(carry.name) #Printing from Employee
# carry.print_from_Student(carry.name)  #Printing from Student
#See the acquisition concept(made by me) in more realistic example

#Multiple Inheritence
class GoodMan(Student, Employee):
# class GoodMan(Student):    #Multilevel Inheritence
    greet = "Good Programming"

    @staticmethod
    def print_from_GoodMan(string):
        print("A Employee and student is goodman")
        return()
    
carry = GoodMan("CarryGupta","Marketing")
carry.about()
carry.print_from_Employee(carry.name)
carry.print_from_Student(carry.name)
carry.print_from_GoodMan(carry.name)
print(carry.greet)

# carry.print_from_GoodMan(carry.work)
# carry.print_from_Student(carry.name)
# carry.print_from_Employee(carry.name)
