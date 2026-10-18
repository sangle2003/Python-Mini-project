def decorator(func):
    def Wrapper(name ):
        print("Welcome ")
        func(name)
    return Wrapper

@decorator 
def greet(name):
    print("hello",name )
    
greet("pradip")