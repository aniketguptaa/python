# Public and Private Protected Access
class Employee:
    _sallary = 256 #Public class variable
    __wife_name = "Jenny" #Private class variable
    pass

carry = Employee()
carry.name = "Carrygupta"
print(carry.name)
print(carry._sallary)
gain_Access_wife = carry._Employee__wife_name 
print(carry._Employee__wife_name)
# print(objectname._classname__classvariable) # <- access to private variable
# name mangling in python
print(carry._Employee__wife_name)
print(gain_Access_wife)

