class Science:
    def about(self):
        return(f"My name is {self.name} and I read in {self.standard}")
#Carry profile
carry = Science()
carry.name = "Carry Gupta"
carry.standard = "X"
print(carry.about())
#Harry profile
harry = Science()
harry.name = "Harry Dev"
harry.standard = "X"
print(harry.about())