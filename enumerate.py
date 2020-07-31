list1 = ["Bhindi", "Tomato", "Chowmein","Egg pakora"]

# i = 0
# for items in list1:
#     if i % 2 != 0:
#         print(f"Please Buy {items}")
#     i+=1 To avoid this we will use Enumerate function

for index , items in enumerate(list1):

    if index % 2 != 0:
        print(f"Please buy {items}")
