# Creating a list with strings
list1 = ["egg", "fish", "chicken"]

print(list1)
print("I love to eat", list1[2]) # Example of indexing

# We can also create list of numbers
number_list = [45, 25, 26]
print(number_list)

# Example of indexing
print("My id number is", number_list[2])

# Example of slicing
print(number_list[:2])

# Example of appending
number_list2 = [45, 25, 454]
number_list2.append(45) # We can print numerous times
number_list2.append(464)
print(number_list2)

# Example of extending
number_list3 = [1,2,3,4,5]
number_list3.extend([6,7,8,9])
print(number_list3)

# Example of concatenation in list
number_list4 = [1,2,3]
print(number_list4 + [4,5,6])

# Example of repeating
l2 = []
print(["Carry"] * 4)

# Example of empty list and appending elements in it
name = []
name.append("Amar")
name.append("Akbar")
name.append("Anthony")
print(name)

# Example of deleting or removing elements in list

l3 = ["Carry", "Garry", "Sharry"]
print(l3)
del l3[1] #Deleting by indexing
# print(l3.pop(0)) #Deleting by using pop() function
# del l3 [2]
print(l3)

# Example of empty a list
l4 = ["Carry", "Larry", "Garry"]
print(l4)
l4.clear()
print(l4)

# Example of reversing elements in list

l5 = [3,2,1]
print(l5)
l5.reverse()
print(l5)

#We can also take it as an input
Name = []
x = input()
y = input()
z = input()
Name.append(x)
Name.append(y)
Name.append(z)
print(Name)

# Example of nested list

nested_list = ["element1", "element2", [454,454,854], "element3", 4.25]
print(nested_list)

# Example of nested list indexing
nested_list2 = ["Name1", "Name2", [2,3,4,5]]
print(nested_list2[1][1])

# Example of sort() function (ascending order)
number_list.sort()
print(number_list)

# Example of max() and min() function
maxnum = max(number_list)
print(maxnum) #Greatest number in list
minNum = min(number_list) #Smallest number in list
print(minNum)
