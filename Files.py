# Writing into a file
with open('text.txt', 'w', encoding = 'utf-8') as data:
    data.write('I am in file')
    data.write('\nI am second line of file')
data.close()

print('I am in compiler')

# Reading from a file
open_data = open('text.txt', 'r', encoding= 'utf-8')
content = open_data.read()
print(content)
open_data.close()
