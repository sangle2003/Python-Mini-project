#local and gloable variable diclearation.
x = 10

def demo():
    x = 20
    
    print("local :: ",x)
    print("gloable :: ",globals()["x"])
    
demo()