# 1. @ staticmethod : which is calledd using classname.staticmethod
# 2. non static : belong to object .
class MathUtils:
    @staticmethod
    def add(a,b):
        return a + b
    
print(MathUtils.add(5,3))

#classname.function()

#func call using object
#m = mathUtils90
#m.add()