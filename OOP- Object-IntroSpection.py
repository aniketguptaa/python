class Object:
    pass

object1 = Object()
object1.attribute = "Name"

print(id(object1.attribute)) #Memory ID

print(dir(object1)) # Consisting files and folder

print(dir(Object))
