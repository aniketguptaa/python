user_name = input("Enter your name: ")
user_age =  input("Enter your age: ")
user_add = input("Enter your address: ")

with open('userdata.txt', 'w', encoding = 'utf - 8') as user_data:
    user_data.write(user_name)
    user_data.write (user_age)
    user_data.write(user_add)
user_data.close()

print('Your details are as follow:')
user_data = open('userdata.txt', 'r', encoding =  'utf-8')
# print_data = user_data.read()
# print(print_data)
# user_data.readline()
for lines in user_data:
    print(lines, end = " \n")
# print(user_data.readline())
# user_data.close()