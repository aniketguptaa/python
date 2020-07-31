#Program to illustrate use For with if-else.

menu = ["Biryani","Mutton","Tandoori Chicken","Chilli Chicken"]

for item in menu:
    if item == "Mutton": # "Chicken Biryani"
        print("Available")
        break
else:
    print("Your item is not available")