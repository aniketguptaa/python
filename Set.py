# Sets are mutable
set1 = {"spam", 3.14, 3.336}
print(set1)

# Tuple in sets
set2 = {'spam', 3.3, ('spamming',3.14)}
print(set2)

# List in sets

set3 = (['spam in list'])
print(type(set3))

a = {}
print(type(a))
b = set()
print(type(b))

set4 = {1,2,3,4}
# set4.add(5) # We can add only one thing
# set4.update(["Spam"]) # We can add multiple data types
set4.update([4,5],{1,6,8})
print(set4)

myset = {1,2,3,4,5}
print(myset)
myset.discard(4)
myset.remove(5)
# myset.clear()
print(myset)

# Doing some mathematics

x = {1,2,3,4,5}
y = {4,5,6,7,8}
print('x union b is ', x | y)
print('x intersection y', x&y)
print('x difference y is ', x - y)
print('x symmetric difference y is ', x^y)