def decorater(any_function):
    def wrapper_function():
        print("This is printed from decorator")
        any_function()
    return wrapper_function

@decorater #shortcut to print
def func1():
    print("This is function 1")
@decorater
def func2():
    print("This is function 2")

# func1 = decorater(func1)
func1()
func2()