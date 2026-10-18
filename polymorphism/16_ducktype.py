class A:
    def show(self):
        print("Class A")
        
class B:
    def show(self):
        print("Class B")
        
objects = [A(), B()]

for obj in objects:
    obj.show()