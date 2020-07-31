class Employee:

    def about(self):
        return(f"Name is {self.name}")
    @staticmethod
    def greeting(names):
        print("Happy Diwali " + names)
        return()

carry = Employee()
carry.name = "CarryGupta"

# print(carry.name)
print(carry.about())

carry.greeting(carry.name)
Employee.greeting("Ramji")   #Alternative method (we can use static method with class name)
