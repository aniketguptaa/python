number = [1,2,3,4,5,6,7,8,9]
sum = 0
for values in number:
    sum = sum + values
print(sum)

# Range function range(initial value , final value, skipping)
print(range(0,10)) # From 0 to 10 range
print(list(range(0, 10))) # create a list from 0 to 10
print(list(range(0,10,2))) # table of 2
print(list(range(3,33,3))) # table of 3

# Printing range list in more readable format
list1 = range(0,20)
for items in list1:
    print(items, end = '\n')

# Iterating through for loop
study = ['Mathematic', 'Physics', 'Chemistry']
for subjects in study:
    print('I like to study', subjects, end = '\n')

# using for loop with else
digits = [5,6,7,8,9]
for i in digits:
    print(i)
else:
    print('Nothing to print')

# using for loop with if else

student_name = 'harry'
marks = {'john': 99, 'harry':80, 'garry': 89}
for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No records')