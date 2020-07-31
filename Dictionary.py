dict = {1 : "spam", 2: "spamming"}
print(dict)

dict1= {'name': 'Carry', 'age': 26}
print(dict1['name'])
print(dict1['age'])

# Adding keys and value in preesxising dictionary
dict1['address'] = 'Silicon valley'
print(dict1['address'])
print(dict1)

squares = {1:1, 2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81, 10:100}
print(squares.pop(4)) # pop up value of key
print(squares)

# Methods in dictionary
marks = {}.fromkeys(['Maths','English','Science'], "very good")

# marks = {}.fromkeys(['Maths','English','Science'], 99)
print(marks)
for item in marks.items():
    print(item)
print(list(sorted(marks.keys())))

# name = {"name":"carry", "age":14}
# print(list(name.keys()))
# print(list(sorted(name.keys()))) it will print sorted values

# Python dictionary comprehension
square = {x : x * x for x in range(6)}
print(square)
# Alternative Methods
# squares = {}
# for x in range(6):
#     squares[x] = x*x
# print(squares)
