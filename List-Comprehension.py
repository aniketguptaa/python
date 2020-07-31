# l1 = [2 ** x for x in range(10)]
# print(l1)

# It can be also written as
# l1 = []
# for x in range(10):
#     l1.append(2**x)
# print(l1)

l2 = [2**x for x in range(10) if x > 5]
print(l2)
odd = [x for x in range(20) if x % 2 == 1]
even = [ x for x in range(20) if x % 2 == 0]
print(odd)
print(even)
l3 = [x+y for x in ["Python ", "C++ "] for y in ["Language", "Tutorial"]]
print(l3)

# Example of membership in list
members = ["Carry", "Garry", "Larry"]
print("Shaun" in members) #False
print("Carry" in members) #True

#Iterating through a list

for fruits in ['apple','mango','banana']:
    print("I Like To Eat", fruits)
    
#Another way to write the program
basket = ['apple','mango','banana', 'pineapple','grapes']
for fruits in basket:
    print("I like to eat", fruits)