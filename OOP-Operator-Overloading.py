class Science:

   def __init__(self,name,marks):
       self.name = name
       self.marks = marks

   def about(self):
       return(f"The name is {self.name} and marks is {self.marks}")
    
    #Dunder Methods
   def __add__(self,other):
       return self.marks + other.marks

   def __repr__(self):
       return(self.about())

   def __str__(self):
       return ("I am printing from str") 

carry = Science("carryGupta", 250)
harry = Science("Harryless", 5)

# print(carry.about())
# print(harry.about())
print(f"Total marks is {carry + harry}")

print(carry) #top priority = str #second priority = repr


# __str__>__repr__