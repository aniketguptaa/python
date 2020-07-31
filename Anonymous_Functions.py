# Anonymous functions is also known as lambda functions

double = lambda x : x  * 2  # one line function, lambda function
print(double(5))

# One line function to print string
hello_name = lambda name: print("Hello", name)
hello_name('Carry')

my_list = [1,2,3,4,5,6,7,8,9]

# Filter function
new_list_filter = list(filter(lambda x : (x % 2 == 0), my_list))
print(new_list_filter)

# Map function
new_list_map = list(map(lambda x : (x *2), my_list ))
print(new_list_map)