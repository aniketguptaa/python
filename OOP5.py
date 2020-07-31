class Employee:
    holiday = 25
    pass
    # Changing class variable
    @classmethod
    def change_holiday(cls,holiday):
        cls.holiday = holiday

carry = Employee()
carry.name = "Carry"

print(Employee.holiday)
# carry.holiday = 26
carry.change_holiday(26)

print(carry.holiday)
# print(carry.name)
print(Employee.__dict__) 