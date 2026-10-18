def my_decorator(func):
    def wrapper():
        print("Before function")
        func()
        print("After function ")
    return wrapper

@my_decorator
def show():
    print("hello")
    print("Welcome")

@my_decorator 
def display():
    print("python")
    print("java")
    
show()
display()