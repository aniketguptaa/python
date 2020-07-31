import os # Importing os module
print(os.getcwd()) # Get current directory 
print(os.listdir()) # List files in current directory

# For printing files in list
list1 = os.listdir()
for items in list1:
    print(items, end = '\n')