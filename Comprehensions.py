# list1  = []
# for items in range(31):
#     if items % 3 == 0:
#         list1.append(items)

# for mains in list1:
#     print(mains)

# list1 = [i for i in range(100) if i %3==0]
# print(list1)

dict1 = {i : f"item{i}" for i in range(10)}
dict2 = {value:key for key,value in dict1.items()}
print(dict1,"\n",dict2)