# Tuples are immutable
t1 = (1,2,3,4,5)
print(t1)

# Example of list in tuple
t2 = ("spam", ["carry",4.25,("I am in tuple")], 3.141,)
print(t2)

# Example of tuple in tuple
t3 = ("Spam",("Spam in 2nd tuple",("Spam in 3rd tuple")))
print(t3)

# Example of tuple without paranthesis() also known as tuple packing
t4 = "spam", 3.14, 256
a, b, c = t4  #Tuple unpacking
print(a,b,c)

# More on tuple
t5 = ("spam") # It is considered as <str>
print(type(t5)) 
t6 = ("Spam",) # It is considered as <tuple>
print(type(t6))

# Indexing in tuple
t7 = ("carry", 3.14, 305)
print(t7)
print(t7[0])
print(t7[1])
print(t7[2])

# Negative indexing in tuple
t8 = ("C","a","r","r","y")
print(t8[-5])
print(t8[-4])
print(t8[-3])
print(t8[-2])
print(t8[-1])

# Slicing in tuple

t9 = ("s","p","a","m")
print(t9[0:4])

# Changing element in Tuple

t10 =  (1,12,123,[121,122])
t10[3][1] = 'Spam'
# t10[3][0] = 365
print(t10)

# Concatenation in tuple
t11  = (1,2,3)
t12  = (4,5,6)
print(t11+t12) #We are joining two tuples

# Repeating a tuple
t13 = ("I am repeating myself",)
print(t13 * 3)

# Deleting

t14 = ('spam', 3.14)
print(t14)
# del t14[0] not possible
del t14
# print(t14)

# Other methods in tuples
t15 = ('spam', 3.14, 3.33,3.33)
print(t15.count(3.33)) # Count the occurence of elements
print(t15.index('spam')) #Position of spam

print('span' in t15)
print('spam' in t15)

# Iterating through a tuple

for items in ('Apple', 'Mango', 'Banana'):
    print(items)
#Alternaive method
t16 = ('Orange', 'Guava', 'Pineapple')
for items in t16:
    print('I like to eat',items)