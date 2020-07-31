#strings are immutable
# Different method of writing string
x = "Hello My name is Carry"
y = 'Hello My name is Carry'
z = '''Hello My name is carry
and i read in class 10 and I am smart'''
print(type(x)) # TypeViewing
print(type(y)) # TypeViewing
print(type(z)) # TypeViewing
print(x)
print(y)
print(z)

# Indexing of string
str = "spamming"
print(str[4]) # print 'm'

# Negative indexing of string
print(str[-1]) # print 'g'

# Slicing in string

print(str[0:8])
# spamming
# Negative slicing 
print(str[:-4])

# Changing a string
str2 =  "C++"
# str[1] = "Spam" Error text ommited
print(str2)
str2 = 'Python' # Replacing C++ with Python
print(str2)
# Del function in string
del str2
# print(str2) # error text ommited

# Concatenation and repeating in string
str3 = "Hello "
str4 = "World"
str5 = str3 + str4
# print(str3+str4)
print(str5)
print(str5 * 2)

# Iterating through a string
count = 0
str6 = "pooling"
for letters in str6:
    if (letters == 'l'):
        count+=1
print(count ," letters found", str6 )

# More complex iteration
count = 0
word = "engineering"
for letters in word:
    if(letters == 'e'):
        count+= 1
print(count," letters founded in", word)

# Membership test

str7 = 'spam'
print('a' in str7) #True
print('g' in str7) #False

# Using Built-in functions
# Enumerate function
str8 = 'commerce'
enum_str8 = list(enumerate(str8))
print(enum_str8)
len_str8 = len(str8)
print(len_str8)

