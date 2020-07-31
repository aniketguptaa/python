class Employee:
    
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@codewithcarry.ml"
    
    def info(self):
        print(f"The Employee is {self.fname} {self.lname}")
    
    @property
    def email(self):
        if self.fname == None or self.lname == None:
            return "Email is not set"
        return f"{self.fname}.{self.lname}@codewithcarry.ml"

    @email.setter
    def email(self,string):
        print('Setting now')
        names = string.split("@")[0]
        self.fname = string.split(".")[0]
        self.lname = string.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None

hindustani_bhau = Employee("Hindustani", "Bhau")
print(hindustani_bhau.email)

# hindustani_bhau.fname = "US"
hindustani_bhau.email = "thisis.hindustani@codewithcarry.ml"
print(hindustani_bhau.email)
print(hindustani_bhau.fname)
del hindustani_bhau.email
print(hindustani_bhau.email)
