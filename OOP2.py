class Employee:
    no_of_days = 10 # Global variable in class (class variable)

carry = Employee()
harry = Employee()

carry.name = "Carry Name"
carry.no_of_days = 11 # Creating instance variable of object

print(carry.no_of_days) 
print(carry.__dict__)
# print(Employee.no_of_days)


# changing class variable
Employee.no_of_days = 28
print(Employee.__dict__)