# This is a tutorial baed on arguments in function

def name(fname, lname):
    print('Your full name is ',fname, lname)

name('Carry', 'Coding')

def sum(x, y): # Formal arguments
    print( x +  y) # Funcion definition

sum(2,4) #Actual arguments


# Variable function arguments
def greet(name, msg = ' Happy Birthday'):
    print('Hello', name + msg)
greet('Carry')