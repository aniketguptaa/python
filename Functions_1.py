# This is the first tutorial of function

# def funcname(parameter_list):
#     pass

def print_function(): 
    print('I am printing from function') # Function definition

print('I am a normal print')
print_function() # Calling a function

# You can call a function numerous time
# print_function()
# print_function()

def greeting(name):
    '''This is example of docstring please dont take it seriously
    '''
    print('Happy Birthday', name)
greeting('Carry')
# Example of docstring
print(greeting.__doc__)
