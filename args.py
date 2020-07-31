# *operator will solve the problem of how multiple 
# values can be passed as arguments
# def total(a,b):
#     return (a+b)
# print(total(4,5,6))

# def new_total(*args): #args is just a general word
#     total = 0
#     for numbers in args:
#         total+=numbers
#     return total
# print(new_total(1,2,3))

#args with normal parameter can not be useful
# def multiply(num,num2,*args):
#     print(num,num2)
#     multiplied = 1
#     for numbers in args:
#         multiplied*= numbers
#     return multiplied
#(1,3 is referencing to num and num2 respectively)

# print(multiply(1,2,3,4)) # (5,6) is taken as args arguments

# args as arguments
# def multiply(*args):
#     multiplied = 1
#     for numbers in args:
#         multiplied*= numbers
#     return multiplied
# num_list = [45,45] # *operator will unpack the elements of list
# print(multiply(*num_list))

