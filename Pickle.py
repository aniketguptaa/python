import pickle

#Picking python objects
# Writing to a file
# cars = ["Audi","BMW", "Mercedes"]
# file = "mycar.pkl"
# fileobj = open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

# Reading a file
file = "mycar.pkl"
fileobj = open(file,'rb')
mycar = pickle.load(fileobj)
print(mycar)
print(type(mycar))