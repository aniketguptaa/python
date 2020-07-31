# Demonstration of Else with finally (try & except)
# f1 = open("text.txt")
try:
    f = open('text.txt')

except Exception as e:
    print(e)
else:
    print('else is running successfully')
# finally:
#     f1.close()   # closing the preopened file
#     print('Finally done')
print('Execution Done')